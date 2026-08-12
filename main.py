from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import User

app = FastAPI(title="Handle Application Logic")

# Allow requests from any device / network / frontend origin.
# For production with a specific frontend, replace "*" with your frontend's URL(s).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = []


@app.get("/")
def home():
    return {
        "message": "Backend API is running"
    }


@app.get("/users")
def get_users():
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return {
        "message": "User created Successfully",
        "user": user
    }
