import time
from flask import Flask
from flask_jwt_extended import create_access_token, JWTManager, decode_token
import uuid
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'KEY'  # Установите секретный ключ для JWT
jwt = JWTManager(app)

load_dotenv()

authorization_limit = int(os.getenv("AUTH_MIN_SESSION")) * 60

def create_uuid():
    return str(uuid.uuid4())

def create_user_token(login: str, password: str) -> str:
    current_time = datetime.now()
    expiration_time = current_time + timedelta(seconds=authorization_limit)

    token = create_access_token(identity={
        "created_time": int(current_time.timestamp()),
        "login": login,
        "password": password,
        "expected_time": int(expiration_time.timestamp())
    })

    return token


with app.app_context():
    token = create_user_token("login", "password")
    print("Encoded Token:", token)

    jwt_decoded_token = decode_token(token)
    print("JWT Decoded Token:", jwt_decoded_token)