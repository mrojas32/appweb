from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.routes import canchas
import uvicorn
import logging

app = FastAPI(title='Wiseguide API Gateway')

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://wiseguide.ai",
    "https://www.wiseguide.ai",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(canchas.router)

if __name__ == "__main__":
    uvicorn.run(
            "app:app",
            port=5000,
            reload=True,
            log_level=logging.DEBUG,
            access_log=True
        )
