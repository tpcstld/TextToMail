from google.appengine.api import mail
import logging
import traceback

def try_send_email(destination_address, email_body):
    try:
        if not mail.is_email_valid(destination_address):
            return False
        
        sender_address = "htht@test.com"
        subject = "htht"
        body = email_body
        mail.send_mail(sender_address, destination_address, subject, body)
        return True
    except:
        logging.error(traceback.format_exc())
        return False
