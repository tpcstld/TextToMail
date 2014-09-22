from google.appengine.api import mail
import logging
import traceback

def try_send_email(destination_address, sender, email_body):
    if email_body.isspace():
        return "Empty Email Body"
    
    try:
        if not "@" in destination_address:
            return "Invalid Destination Address \"" + destination_address +"\""
        
        sender_address = "TextToMail <tpcstld-sms@appspot.gserviceaccount.com>"
        subject = "Text to Mail"
        body = email_body + "\n\nSent from " + sender + " using TextToMail"
        mail.send_mail(sender_address, destination_address, subject, body)
        return "OK"
    except:
        logging.error(traceback.format_exc())
        return "Unknown Error"
