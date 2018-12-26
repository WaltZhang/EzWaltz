import smtplib
from email.message import EmailMessage
import email.utils

import config

class SSLSmtpMail
    def __init__(mailhost, port, fromaddr, toaddrs, record, username, password, secure=None):
        self.mailhost = mailhost
        self.port = port
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.record = record
        self.username = username
        self.password = password
        self.secure = secure

    def sending_mail(subject, message):
        port = self.mailport
        if not port:
            port = smtplib.SMTP_SSL_PORT
        smtp = smtplib.SMTP_SSL(self.mailhost, port, timeout=self.timeout)
        msg = EmailMessage()
        msg['From'] = self.fromaddr
        msg['To'] = ','.join(self.toaddrs)
        msg['Subject'] = subject
        msg['Date'] = email.utils.localtime()
        msg.set_content(message)
        if self.username:
            if self.secure is not None:
                smtp.ehlo()
                smtp.starttls(*self.secure)
                smtp.ehlo()
            smtp.login(self.username, self.password)
        smtp.send_message(msg)
        smtp.quit()
