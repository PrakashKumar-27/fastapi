from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35}
}

class User(BaseModel):
    id: int
    name: str
    age: int

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_db.get(user_id)
    if not user:
        return {"error": "User not found"}
    return {"id": user_id, **user}

@app.put("/users/{user_id}")    
def update_user(user_id: int, name: str = None, age: int = None):
    user = user_db.get(user_id)
    if not user:
        return {"error": "User not found"}
    if name:
        user["name"] = name
    if age:
        user["age"] = age
    return {"message": "User updated successfully", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = user_db.pop(user_id, None)
    if not user:
        return {"error": "User not found"}
    return {"message": "User deleted successfully"}