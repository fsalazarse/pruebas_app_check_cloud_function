from firebase_functions import https_fn
from firebase_admin import initialize_app, app_check
from app_check.app_check import App_check
import jwt

initialize_app()

@https_fn.on_request(max_instances=10, timeout_sec=120)
def test_get_functions(req: https_fn.Request) -> https_fn.Response:
    # Configuración de encabezados CORS
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Firebase-AppCheck"
    }

    # Manejar solicitudes OPTIONS preflight
    if req.method == "OPTIONS":
        return https_fn.Response("", headers=headers)

    try:

        Ins_app_check = App_check(app_check_token)
        # Obtener token del app_check
        app_check_token = req.headers.get("X-Firebase-AppCheck", default="")
        #Validar si el token es valido
        validate_token = Ins_app_check.validate_token(app_check)
        print(validate_token)
   
        return https_fn.Response("Success", headers=headers)

    except ValueError as error:
        # Captura específica de la excepción ValueError y devuelve una respuesta de error con el mensaje
        return https_fn.Response(f"Error: {error}", headers=headers, status=500)

    except Exception as error:
        # Captura de otras excepciones y devuelve una respuesta de error genérica
        return https_fn.Response(f"Error: {error}", headers=headers, status=500)


   


