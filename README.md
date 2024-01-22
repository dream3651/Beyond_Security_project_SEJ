# 💻매장내 범죄현상 감지 

- 매장에서 발생하는 범죄를 모니터링 통해 감지
- 이상행동 감지시 알림톡을 통해 문자 전송

---
## 🗒️Subject
<img width="1048" alt="무제10" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/c652e1ff-4709-4ad0-8159-572ecdfe9163">

## 📌purpose
<img width="765" alt="무제11" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/7f1fe399-4a73-42b3-aa11-30850d6413b9">

## 📝workflow
<img width="890" alt="무제12" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/abe56a99-626a-4a0f-afba-ae34bc54b434">


## 2D CNN
<img width="1227" alt="무제2" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/d8c31afa-e40d-4ada-9da2-4dad042f5882">

- 동영상 파일내 이상행동 구간만 프레임으로 나눔
- 프레임으로 나눠진 이미지 크기를 조정하고 배열 변환 및 정규화
- 2D_CNN을 이용해 이미지내 특징 학습
- 배경을 제외한 사람의 형상만 학습시키기 위해 media-pipe를 이용해 관절 부부만 추출 
- 추출된 관절 이용해 이미지로 학습

## CNN + LSTM
<img width="1230" alt="무제4" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/d2646983-2d3b-4426-911d-35d568945634">

- 행동이 발생되는 구간의 프레임만 추출 및 크기조정, 흑백 변환
- 배열 변환, 정규화 후 시퀀스를 구성
- 일정 부분의 프레임이 겹치도록 시퀀스 구성
- 데이터 증강을 통해 모델 일반화 및 CNN을 통해 공간적 특징 추출

## WEB
<img width="1226" alt="무제7" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/381aee17-dfc1-4468-bb4f-ad79abd7a3d5">

- Django를 이용해 web page구현
- 원본 영상과 시연영상을 비교할수 있도록 모달을 이용해 비교영상 구현

## 📌Purpose attainment
<img width="1221" alt="무제8" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/874ed7bf-6b84-46de-90c0-c453de8c5fcf">

## 🗂️Documents
<img width="1233" alt="무제9" src="https://github.com/Hoon-Code/face_recognization_project/assets/145303974/40da03e0-fd90-48de-8e82-09d57413b1bf">




