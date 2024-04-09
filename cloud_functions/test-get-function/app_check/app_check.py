from dataclasses import dataclass
import jwt

@dataclass
class App_check:
    app_check_token: str 

    def validate_token(self, app_check):
        
        try:
            #Verificar si el token es valido
            verify_token = app_check.verify_token(self.app_check_token)
            return verify_token
        # Si el token no es valido
        except (ValueError, jwt.exceptions.DecodeError):
            #Enviar una respuesta de error 
            raise ValueError("Invalid Token")
        
        
