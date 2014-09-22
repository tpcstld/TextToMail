from flask import Flask
from flask import request
from flask import render_template
import mailer
app = Flask(__name__)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/sms', methods=['GET', 'POST'])
def api_sms():
    if request.method == 'POST':
        sms_message = request.values.get("Body", None)
        sender = request.values.get("From", None)
        if sms_message is None or sender is None:
            return render_template("sms_error.xml")
        try:
            destination_address, body = sms_message.split(' ', 1)
        except:
            return render_template("sms_error.xml")
        if not mailer.try_send_email(destination_address, sender, body):
            return render_template("sms_error.xml")

        return render_template("sms_success.xml")
    
    return "HTHT"

@app.route('/')
def test():
    return "HELLO WORLD"


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
