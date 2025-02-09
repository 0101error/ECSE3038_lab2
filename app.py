from fastapi import FastAPI

app = FastAPI()

data = []

@app.get("/person")
async def get_people():
    return data


# This is a route for POST requests to /person.
# It's used to add new person data to our 'data' list.
@app.post("/person")
async def add_person(person_data: dict):  # We expect a dictionary as input

    # Let's check if the request data has the required keys: 'name', 'occupation', 'address'
    if "name" in person_data and "occupation" in person_data and "address" in person_data:
        name = person_data["name"]
        occupation = person_data["occupation"]
        address = person_data["address"]

        # Now, let's check if the values for name, occupation, and address are not empty strings.
        if name and occupation and address:  # Short way to check if strings are not empty
            new_person = {
                "name": name,
                "occupation": occupation,
                "address": address
            }
            data.append(new_person)  # Add the new person to our data list

            # Return a success response
            return {"success": True, "result": new_person}
        else:
            # If any of the values are empty, it's an invalid request
            return {"success": False, "result": {"error_message": "invalid request - fields cannot be empty"}}
    else:
        # If any of the required keys are missing in the request, it's also an invalid request
        return {"success": False, "result": {"error_message": "invalid request - missing required keys (name, occupation, address)"}}
