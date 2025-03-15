import datetime
import random
import smtplib
import pandas

FROM_EMAIL_ADDRESS = "senderemail"
PASSWORD = "password"

current_datetime = datetime.datetime.now()
current_day = current_datetime.day
current_month = current_datetime.month

birthday_df = pandas.read_csv("birthdays.csv")
for index, row in birthday_df.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        with open(f"/path/letter_templates/"
                  f"letter_{random.randint(1,3)}.txt", mode="r") as file_letters:
            letter = file_letters.read()
            personalised_letter = letter.replace("[NAME]", row["name"])

        with smtplib.SMTP_SSL("smtp.mail.ru", 465) as connection:
            connection.login(user=FROM_EMAIL_ADDRESS, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL_ADDRESS,
                to_addrs=row["email"],
                msg=f"Subject: Happy Birthday! \n{personalised_letter}")
