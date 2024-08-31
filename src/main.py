"""
This module contains the main functionality of the application.
It sets up a FastAPI application with a single endpoint for retrieving a name.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/name")
def get_name():
    """
    Retrieve the name for the application.

    Returns:
        str: A string containing the name of the application.
    """
    return "this is my name the mohan who are you yo fucker"
