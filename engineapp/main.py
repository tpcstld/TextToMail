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
        body = request.values.get("Body", None)
        if body is None:
            return render_template("sms_error.xml")
        
        if not mailer.try_send_email("jerryjiang1128@gmail.com", body):
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
