import smtplib
import os
import dotenv
dotenv.load_dotenv(dotenv_path="/Users/zamiraignatova/PycharmProjects/day_39_/.venv/.env")

class NotificationManager:
    def __init__(self):
        """This class is responsible for sending notifications with the deal flight details"""
        self._password = os.environ["EMAIL_PASSWORD"]
        self._from_email_address = os.environ["EMAIL_ADDRESS"]
        self._smtp_host = os.environ["SMTP_SERVER_ADDRESS"]
        self._smtp_port = int(os.environ["SMTP_PORT"])


    def send_email(self, email_list, message_body):
        with smtplib.SMTP_SSL(self._smtp_host, self._smtp_port) as connection:
            connection.login(user=self._from_email_address, password=self._password)
            for email_address in email_list:
                connection.sendmail(from_addr=self._from_email_address, to_addrs=email_address,
                    msg=f"Subject:PRICE ALERT!🚨\n{message_body}".encode('utf-8'))
