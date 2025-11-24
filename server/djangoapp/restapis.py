# Uncomment the imports below before you add the function code
import requests
import os
import json
# from .models import CarDealer, DealerReview  # COMMENTED OUT - Not needed for this lab
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

# FIXED: Removed "http://" from the beginning since the URL already has "https://"
backend_url = os.getenv(
    'backend_url', 
    default="https://pauloralus-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai")

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """
    Make a GET request to the backend API
    Args:
        endpoint: API endpoint to call
        **kwargs: URL parameters as keyword arguments
    Returns:
        JSON response from the API
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    
    request_url = backend_url + endpoint + "?" + params
    
    print("GET from {} ".format(request_url))
    
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")
        return None


def analyze_review_sentiments(text):
    """
    Analyze sentiment of review text using microservice
    Args:
        text: Review text to analyze
    Returns:
        JSON response with sentiment (positive/negative/neutral)
    """
    request_url = sentiment_analyzer_url + "analyze/" + text
    
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    """
    Post a review to the backend API
    Args:
        data_dict: Dictionary containing review data
    Returns:
        JSON response from the API
    """
    request_url = backend_url + "/insert_review"
    
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
        return None