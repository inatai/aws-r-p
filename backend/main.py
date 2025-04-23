# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Reactと通信できるようにする
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番では制限すべき
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def read_root():
    return {"message": "AWS Hello from FastAPI!"}
