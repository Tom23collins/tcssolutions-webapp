import os
AUTHORITY= f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}"

# Application (client) ID of app registration
CLIENT_ID = os.getenv("CLIENT_ID")
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
 
REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.

ENDPOINT = 'https://graph.microsoft.com/v1.0/me'  
SCOPE = ['User.ReadBasic.All']

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"

# Database configuration
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_KEY')
DB_NAME = os.getenv('DB_NAME')