from fastapi import FastAPI
from custom_middleware import add_real_ip_header
from main import app as original_app

app = FastAPI()
app.middleware('http')(add_real_ip_header)
app.include_router(original_app.router)
