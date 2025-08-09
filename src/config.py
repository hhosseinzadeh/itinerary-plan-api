import os

from pyngrok import ngrok
import nest_asyncio
from openai import OpenAI
import firebase_admin
from firebase_admin import credentials, firestore



NGROK_AUTH_TOKEN = "YOUR-NGROk-AUTH-TOKEN"
OPENAI_API_KEY = "YOUR-OPENAI_API_KEY"
FIREBASE_CRED_PATH = "YOUR_FIREBASE_PRIJECT_DATABASE.json"

# Ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
nest_asyncio.apply()

# OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Firebase
cred = credentials.Certificate(FIREBASE_CRED_PATH)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()
