from dataclasses import dataclass
import jwt

@dataclass
class App_check:
    app_check_token: str 

    def validate_token(self, app_check):
        
        try:
            verify_token = app_check.verify_token(self.app_check_token) #Verificar si el token es valido
            return True # Si el token es valido retornar True
        # Si el token no es valido
        except (ValueError, jwt.exceptions.DecodeError):
          
            raise ValueError("Invalid Token")   #Enviar una respuesta de error 
        
        
