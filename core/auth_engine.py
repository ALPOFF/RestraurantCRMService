import os

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthEngine:
    hash_engine = CryptContext(schemes=["bcrypt"])
    secret = os.environ.get("secret")

    def hash_password(self, password: str):
        return self.hash_engine.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        return self.hash_engine.verify(password, hashed_password)

    def encode_token(self, login):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
            "sub": login
        }
        return jwt.encode(payload, self.secret, algorithm=os.environ.get("algorithm"))

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=os.environ.get("algorithm"))
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
