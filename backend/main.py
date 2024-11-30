from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import interviewRoutes
app = FastAPI()

origins = [
    "http://localhost:3000/",
    "http://localhost:5000/",
    "http://localhost:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(interviewRoutes.router, prefix='api/')
