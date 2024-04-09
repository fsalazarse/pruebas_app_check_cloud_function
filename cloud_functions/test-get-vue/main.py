# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app

initialize_app()



@https_fn.on_request()
def test_vue(req: https_fn.Request) -> https_fn.Response:
    try:
        return https_fn.Response("Hello world!")
    except Exception as error:
         return https_fn.Response(f"error {error}", status=500)