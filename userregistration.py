
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserRegistrationRequest(BaseModel):
	username: str
	email: EmailStr
	password: str = Field(..., min_length=8)

@app.post("/register")
def register_user(user: UserRegistrationRequest):
	# Here you would add logic to save the user, check for duplicates, etc.
	return {"message": f"User '{user.username}' registered successfully."}
