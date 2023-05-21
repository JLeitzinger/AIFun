import os
from cred.credentials import creds

# Set all the environment variables
for key,interVal in creds.items():
    for subkey, value in interVal.items():
        envKey = f'{key}_{subkey}'
        os.environ[envKey] = value
