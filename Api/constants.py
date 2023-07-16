import os

SENDER_EMAIL = "komalsaikiran05@gmail.com"
RECEIVER_EMAIL = ["komalsaikiran05@gmail.com", "ushavenkateswararao100@gmail.com", "upskillzone.social@gmail.com"]
EMAIL_PASSWORD = "nssonhmvdadwylxd" #os.environ.get('EMAIL_PASSWORD')  # "nssonhmvdadwylxd"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 # os.environ.get('SMTP_PORT')  # 587
MESSAGE = "Hi Team,\n\nYou are attended Python sessions.\n\nThanks,\nPython Trainer"

print(EMAIL_PASSWORD)
print(SMTP_PORT)