from logging.handlers import SMTPHandler


# Provide a class to allow SSL (Not TLS) connection for mail handlers
class SSLSMTPHandler(SMTPHandler):
    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            from mail.ssl_email import SSLSmtpMail

            port = self.mailport
            if not port:
                port = smtplib.SMTP_SSL_PORT
            ssl_mail = SSLSmtpMail(self.mailhost,
                                   port,
                                   fromaddr=self.fromaddr,
                                   toaddrs=self.toaddrs,
                                   username=self.username,
                                   password=self.password,
                                   secure=self.secure,
                                   timeout=self.timeout)
            ssl_mail.sending_mail(self.getSubject(record), self.format(record))
        #     import smtplib
        #     from email.message import EmailMessage
        #     import email.utils
        #
        #     port = self.mailport
        #     if not port:
        #         port = smtplib.SMTP_SSL_PORT
        #     smtp = smtplib.SMTP_SSL(self.mailhost, port, timeout=self.timeout)
        #     msg = EmailMessage()
        #     msg['From'] = self.fromaddr
        #     msg['To'] = ','.join(self.toaddrs)
        #     msg['Subject'] = self.getSubject(record)
        #     msg['Date'] = email.utils.localtime()
        #     msg.set_content(self.format(record))
        #     if self.username:
        #         if self.secure is not None:
        #             smtp.ehlo()
        #             smtp.starttls(*self.secure)
        #             smtp.ehlo()
        #         smtp.login(self.username, self.password)
        #     smtp.send_message(msg)
        #     smtp.quit()
        except Exception:
            self.handleError(record)
