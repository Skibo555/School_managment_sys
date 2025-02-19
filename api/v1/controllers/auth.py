import datetime

import jwt
from decouple import config


class AuthManager:

    @staticmethod
    def encode_token(user_data):

        try:

            payload = {
                "id": str(user_data.id),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=180)
            }
            return jwt.encode(payload=payload, key=config("JWT_SECRET_KEY"), algorithm="HS256")
        except Exception as ex:
            raise ex





