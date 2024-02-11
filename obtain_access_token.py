import base64
import requests
from spotify_credentials import spotify_client_id, spotify_client_secret

# Format the credentials how the Spotify web API expects them to be when passed in the authorization header.
# Encode the credentials in Base64 and decode them.
# Decoding the credentials converts them from a byte object to a string object.
spotify_client_credentials = base64.b64encode(f"{spotify_client_id}:{spotify_client_secret}".encode()).decode()

# Create authorization header to be passed to obtain the "access_token" to make API calls.
authorization_headers = {
    "Authorization": f"Basic {spotify_client_credentials}"
}

# Create authorization body to be passed to obtain the "access_token" to make API calls.
authorization_body = {
    "grant_type": "client_credentials"
}

# Set the authorization URL to be used to obtain the "access_token" to make API calls.
authorization_url = "https://accounts.spotify.com/api/token"

# Make POST request to authorization token URL and store results in the "authorization_token_response" variable.
authorization_response = requests.post(authorization_url, data = authorization_body, headers = authorization_headers)

if authorization_response.status_code != 200:
    print("Failed to obtain access token.")
elif authorization_response.status_code == 200:
    # Store the "access_token" value to make API calls to the "access_token" variable.
    access_token = authorization_response.json()['access_token']
    # Store the "token_type" value to make API calls to the "token_type" variable.
    token_type = authorization_response.json()['token_type']
    # Store the "expires_in" value to make API calls to the "expires_in" variable. 
    expires_in = authorization_response.json()['expires_in']
    print("Obtained access token successfully.")
    print(f"Access token: {access_token}")
    print(f"Token type: {token_type}")
    print(f"Expires in: {expires_in}")