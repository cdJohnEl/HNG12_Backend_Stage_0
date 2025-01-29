from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get("/")
def get_info():
    return {
        "email": "easykelchimdikejohn@gmail.com", 
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/cdJohnEl/HNG12_Backend_Stage_0.git" 
    }

