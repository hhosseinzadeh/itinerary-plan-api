from fastapi import FastAPI
from pyngrok import ngrok
import uvicorn
from routes import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    public_url = ngrok.connect(8000)
    print(f"Public URL: {public_url}")
    uvicorn.run(app, port=8000)
