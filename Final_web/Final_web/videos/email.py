# email_utils.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email(last_email_time):
    current_time = time.time()
    if current_time - last_email_time < 300:  # 5분 간격으로 이메일 전송 제한
        return last_email_time, False

    # 이메일 설정
    gmail_user = 'sej365@gmail.com'
    gmail_password = 'tecc xhwj rrxy dvxf'
    sent_from = gmail_user
    to = ['eun_ju_son@naver.com']
    subject = '이상행동 감지'
    body = '이상행동이 감지됐습니다.'

    # 이메일 구성
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = ", ".join(to)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # 이메일 전송
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, msg.as_string())
        smtp_server.close()
        print("Email sent successfully!")
        return current_time, True
    except Exception as ex:
        print("Something went wrong...", ex)
        return last_email_time, False