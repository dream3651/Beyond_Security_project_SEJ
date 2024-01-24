import cv2
import numpy as np
from tensorflow.keras.models import load_model
import uuid
import os
from django.conf import settings
from videos.email import send_email
from PIL import Image, ImageDraw, ImageFont

def apply_model(video_path):
    # 모델 및 클래스 이름 설정
    model_path = os.path.join(settings.BASE_DIR, 'CNN_LSTM_11.h5')
    model = load_model(model_path)
    class_names = {0: '파손', 1: '구매', 2: '폭행', 3: '이동',4:'절도'}


    cap = cv2.VideoCapture(video_path)

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    output_filename = f'output_video_{uuid.uuid4()}.mp4'
    output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
    fourcc = cv2.VideoWriter_fourcc(*'x264')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frame_buffer = []
    predictions_buffer = []

    last_email_time = 0  # 이메일 전송 시간 추적을 위한 초기값

    # 한글 폰트 경로 지정 (시스템에 설치된 한글 폰트 경로를 사용)
    font_path = "C:/Windows/Fonts/malgun.ttf"
    font_size = 50
    font = ImageFont.truetype(font_path, font_size)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        resized_frame = cv2.resize(frame, (100, 100))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        normalized_frame = gray_frame / 255.0
        frame_buffer.append(normalized_frame.flatten())

        if len(frame_buffer) == 20:
            input_data = np.array(frame_buffer)
            input_data = input_data.reshape(1, 20, 100, 100, 1)
            predictions = model.predict(input_data)
            predicted_class = class_names[np.argmax(predictions[0])]
            predictions_buffer.append(predicted_class)
            frame_buffer = []

        #이메일 발송 조건 확인 및 처리
        if predictions_buffer and predictions_buffer[-1] in ['파손', '폭행', '절도']:
            last_email_time, email_sent = send_email(last_email_time)
            if email_sent:
                predictions_buffer = []  # 이메일 전송 후 버퍼 초기화

        # 프레임에 예측 결과 표시
        if predictions_buffer:
            # OpenCV 프레임을 PIL 이미지로 변환
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(frame_pil)

            # 이미지에 텍스트 추가
            text = f"행동: {predictions_buffer[-1]}"
            draw.text((50, 50), text, font=font, fill=(255, 0, 0))  # 적절한 위치와 색상 설정

            # PIL 이미지를 OpenCV 이미지로 다시 변환
            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

            # text = f"행동: {predictions_buffer[-1]}"
            # cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

        out.write(frame)

    cap.release()
    out.release()

    return output_path