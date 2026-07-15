import smtplib
import os
from email.message import EmailMessage

print("===== EMAIL SENDER =====")

sender_email = input("Sender Email: ")
app_password = input("App Password: ")
receiver_email = input("Receiver Email: ")

subject = input("Subject: ")
body = input("Message: ")

attachment = input("Attachment File Path: ")

message = EmailMessage()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.set_content(body)

if os.path.exists(attachment):

    with open(attachment, "rb") as file:

        file_data = file.read()
        file_name = os.path.basename(attachment)

    message.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

else:
    print("⚠️ Attachment not found. Sending email without attachment.")

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    smtp.starttls()

    smtp.login(sender_email, app_password)

    smtp.send_message(message)

    smtp.quit()

    print("\n✅ Email Sent Successfully!")

except Exception as e:
    print("\n❌ Failed to Send Email")
    print(e)
