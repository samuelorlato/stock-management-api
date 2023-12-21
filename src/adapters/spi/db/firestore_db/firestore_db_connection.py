from src.domain.errors.errors import InternalError

from src.application.interfaces.spi.db_interface import DbInterface

from firebase_admin import credentials, initialize_app

from google.cloud import firestore

class FirestoreDbConnection(DbInterface):
    def __init__(self) -> None:
        try:
            self.connection()

        except Exception as exception:
            raise InternalError("Connection error", original_exception=exception)
    
    def connection(self) -> None:
        credentials = credentials.Certificate("../../configs/credentials.json")
        firebase_app = initialize_app(credentials)

        self.database = firestore.Client()

    def get_db(self):
        return self.database