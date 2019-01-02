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
        except Exception:
            self.handleError(record)
