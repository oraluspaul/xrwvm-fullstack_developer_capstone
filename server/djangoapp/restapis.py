# Uncomment the imports below before you add the function code
import requests
import os
import json
# from .models import CarDealer, DealerReview  # COMMENTED OUT - Not needed for this lab
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

# Get backend URLs from environment variables
backend_url = os.getenv(
    'backend_url', 
    default="https://pauloralus-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai")

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="https://sentianalyzer.234fsqgpn0wp.us-south.codeengine.appdomain.cloud/")


def get_request(endpoint, **kwargs):
    """
    Make a GET request to the backend API
    
    Args:
        endpoint (str): API endpoint to call (e.g., "/fetchDealers")
        **kwargs: URL parameters as keyword arguments
        
    Returns:
        dict: JSON response from the API, or None if error occurs
        
    Example:
        get_request("/fetchDealers")
        get_request("/fetchDealer", id="1")
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
    except Exception as err:
        # If any error occurs
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """
    Analyze sentiment of review text using microservice
    
    Args:
        text (str): Review text to analyze
        
    Returns:
        dict: JSON response with sentiment (positive/negative/neutral)
        
    Example:
        analyze_review_sentiments("Great service!")
        # Returns: {"sentiment": "positive"}
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
        data_dict (dict): Dictionary containing review data with keys:
            - dealership: Dealer ID
            - review: Review text
            - purchase: Boolean indicating if purchase was made
            - purchase_date: Date of purchase (if applicable)
            - car_make: Car make
            - car_model: Car model
            - car_year: Car year
            
    Returns:
        dict: JSON response from the API, or None if error occurs
        
    Example:
        post_review({
            "dealership": 1,
            "review": "Excellent service!",
            "purchase": True,
            "purchase_date": "2024-11-24",
            "car_make": "Toyota",
            "car_model": "Camry",
            "car_year": 2023
        })
    """
    request_url = backend_url + "/insert_review"
    
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None