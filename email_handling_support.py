import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailHandlingSupport:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, to, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, to, text)
        server.quit()

    def read_email(self):
        # TODO: Implement this method to read an email
        pass