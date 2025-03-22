from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict


app = FastAPI()

data: List[Dict] = []

class UserProfileCreate(BaseModel):
    fullName: str 
    occupation: str     
    address: str 


@app.post("/person") 
async def create_user_profile(data: UserProfileCreate): 
    
    if not data.fullName or not data.occupation or not data.address: 
        return {"success": False, "result": {"error_message": "invalid profile request"}} 


    new_entry = {
        "name": data.fullName ,
        "occupation": data.occupation,
        "address": data.address
    }
    data.append(new_entry)

    return {"success": True, "result": new_entry} 

@app.get("/person") 
async def get_user_profiles() -> List[Dict]: 
    
    return data 
