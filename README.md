# ECSE3038 Lab 2 - FastAPI POST Request Handlers

This repository contains a FastAPI application that demonstrates handling POST requests to add person data and GET requests to retrieve person data.

## Function Summaries

### `GET /person`
Retrieves a list of all people currently stored in the application's data. Returns a JSON array of person objects.

### `POST /person`
Adds a new person to the application's data. Expects a JSON request body with "name", "occupation", and "address" fields.
- Returns a success response (status 200) with `{"success": true, "result": {person_data}}` if the request is valid.
- Returns an error response (status 400) with `{"success": false, "result": {"error_message": "invalid request"}}` if the request body is invalid (missing or empty fields).
- Returns a 422 error if the request body doesn't conform to the expected JSON structure.

## Purpose of the Code

This code was written for ECSE3038 Lab 2 to practice building POST request handlers in FastAPI and to understand request validation and response structures.

## My Favourite Pokemon

My favourite Pokemon is **Gengar**. I like Gengar because it's a mischievous Ghost/Poison type. Reminds me of me so i like it 