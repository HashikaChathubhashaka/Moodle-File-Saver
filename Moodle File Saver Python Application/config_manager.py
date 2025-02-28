import os
import json

# config file to save latest file location
CONFIG_FILE = "config.json"


# Function to load the saved folder
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                data = json.load(file)
                if "destination_folder" in data:
                    return data
        except (json.JSONDecodeError, IOError):
            print("Error reading config file. Resetting to default.")

    # Return default if file is missing or invalid
    return {"destination_folder": ""}


# Function to save the selected folder
def save_config(destination_folder):
    with open(CONFIG_FILE, "w") as file:
        json.dump({"destination_folder": destination_folder}, file)
