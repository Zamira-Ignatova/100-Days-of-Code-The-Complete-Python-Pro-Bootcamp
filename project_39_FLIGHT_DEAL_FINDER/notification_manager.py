import smtplib
import os
import dotenv
dotenv.load_dotenv(dotenv_path="/Users/zamiraignatova/PycharmProjects/day_39_/.venv/.env")

class NotificationManager:
    def __init__(self):
        """This class is responsible for sending notifications with the deal flight details"""
        self._password = os.environ["EMAIL_PASSWORD"]
        self._from_email_address = os.environ["EMAIL_ADDRESS"]

    def send_email(self, to_email_address, message):
        with smtplib.SMTP_SSL("smtp.mail.ru", 465) as connection:
            connection.login(user=self._from_email_address, password=self._password)
            connection.sendmail(
                from_addr=self._from_email_address,
                to_addrs=to_email_address,
                msg=f"{message}")
