from google.appengine.api import mail
import logging
import traceback

def try_send_email(destination_address, sender, email_body):
    if destination_address is None or sender is None or email_body is None:
        return False
    
    try:
        if not mail.is_email_valid(destination_address):
            return False
        
        sender_address = "Test Email <jerryjiang1128@gmail.com>"
        subject = "Text to Mail"
        body = "Sent by: " + sender + "\n\n" + email_body
        mail.send_mail(sender_address, destination_address, subject, body)
        return True
    except:
        logging.error(traceback.format_exc())
        return False
