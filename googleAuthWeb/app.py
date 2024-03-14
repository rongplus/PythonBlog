from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management

# Configure Google OAuth
oauth = OAuth(app)
google = oauth.remote_app(
    "google",
    consumer_key="801857933570-sk273ci5luntet2lb23pimn05rihhngm.apps.googleusercontent.com",
    consumer_secret="cceXInp4s8emTNO4Drpq4UPm",
    request_token_params={"scope": "email"},
    base_url="https://www.googleapis.com/oauth2/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
)

@app.route("/")
def home():
    return google.authorize(callback=url_for("authorized", _external=True))
    return "Welcome to my Flask web app!"

@app.route("/login")
def login():
    return google.authorize(callback=url_for("authorized", _external=True))

@app.route("/logout")
def logout():
    session.pop("google_token", None)
    return redirect(url_for("home"))

@app.route("/login/authorized")
def authorized():
    response = google.authorized_response()
    if response is None or response.get("access_token") is None:
        return "Access denied: Reason={}".format(request.args["error_reason"])
    session["google_token"] = (response["access_token"], "")
    return redirect(url_for("home"))

@google.tokengetter
def get_google_oauth_token():
    return session.get("google_token")

if __name__ == "__main__":
    app.run(debug=True)
