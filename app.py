import requests

# Example Gemini API base URL - replace with actual endpoint
GEMINI_API_BASE_URL = "https://api.gemini.com/v3.5"

def get_gemini_data(endpoint):
    """
    Function to make a GET request to the Gemini API endpoint.
    """
    url = f"{GEMINI_API_BASE_URL}/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API request error: {e}")
        return None

def main():
    # Example: fetching market data from Gemini API
    endpoint = "markets"
    data = get_gemini_data(endpoint)
    
    if data:
        print("Gemini API Data:")
        print(data)
    else:
        print("Failed to retrieve data from Gemini API.")

if __name__ == "__main__":
    main()
