from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/sms', methods=['GET', 'POST'])
def api_sms():
    if request.method == 'POST':
        request_json = request.get_json()
        return render_template("sms.xml", message=request_json.get("Body", "Nothing"))
    
    return "HTHT"

@app.route('/')
def test():
    return "HELLO WORLD"


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
