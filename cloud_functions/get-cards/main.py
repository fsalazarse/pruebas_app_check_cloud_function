import firebase_admin
from firebase_functions import https_fn
from firebase_admin import app_check
import flask
import jwt

firebase_app = firebase_admin.initialize_app()
flask_app = flask.Flask(__name__)

@flask_app.before_request
def verify_app_check() -> None:
    app_check_token = flask.request.headers.get("X-Firebase-AppCheck", default="")
    try:
        app_check_claims = app_check.verify_token(app_check_token)
        # If verify_token() succeeds, okay to continue to route handler.
    except (ValueError, jwt.exceptions.DecodeError):
        flask.abort(401)


@flask_app.route("/testToken")
def your_api_endpoint(request: flask.Request):
    
    return "Hello world!"


# Cloud Functions
@https_fn.on_request(max_instances=10, timeout_sec=120)
def plugin_03_v1_test_app_check(req: https_fn.Request) -> https_fn.Response:

    """
        Función de entrada para cloud functions
    """

    with flask_app.request_context(req.environ):
        return flask_app.full_dispatch_request()
