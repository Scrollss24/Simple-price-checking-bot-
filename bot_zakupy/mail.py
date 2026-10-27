import smtplib
from email.message import EmailMessage
def email_message(to,):
    message = EmailMessage()

    message["Subject"] = "price update"
    message["From"] = "b48209050@gmail.com"
    message["To"] = to
    message.set_content(f"Your product price is below your max price. Go and buy it!!!")

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "b48209050@gmail.com"
    sender_password = "ywcj czrl ggwq xuat"
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)