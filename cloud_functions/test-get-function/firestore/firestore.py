from dataclasses import dataclass
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


@dataclass
class Firestore:

    def get_docs(self):
        try:
        
            db = firestore.client() #iniciar servicio de firestore
            docs_stream = db.collection("cards").stream() #obtener documentos de la coleccion cards
            docs = [] # lista de todos los documentos
            for doc in docs_stream:

                docs.append(doc) #agregar documentos a la lista

            return docs #retornar los documentos

        except ValueError as error:
            #Enviar una respuesta de error 
            raise error