#Importing libraries
from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware

class CORSHelper:
    #CORS setup
    def setup_cors(app: FastAPI):
        origins = []
        
        if os.getenv("ENV") == "development":
            origins = ["*"]          
        else:
            origins = ["*"]
            
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )