import smtplib
from email.message import EmailMessage
import email.utils


class SSLSmtpMail:
    def __init__(self, mailhost, mailport, fromaddr, toaddrs, username, password, secure=None, timeout=0):
        self.mailhost = mailhost
        self.mailport = mailport
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.username = username
        self.password = password
        self.secure = secure
        self.timeout = timeout

    def sending_mail(self, subject, message):
        smtp = smtplib.SMTP_SSL(self.mailhost, self.mailport, timeout=self.timeout)
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
