# ==========================================

# Project: Moodle File Saver
# Date: 2021/09/26
# Version: 1.0
# Author: Hashika Chathubhashaka

# Description:
# This Python automation application retrieves the course name and course ID
# from the browser extension and saves files in the corresponding folder
# based on the course name.

# ==========================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import shutil
import threading

from gui_manager import open_gui, get_main_destination_folder

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define a route to move files
@app.route('/move_files', methods=['POST'])
def move_files():
    main_destination_folder = get_main_destination_folder()
    data = request.json
    source_file = data.get('source_file')
    destination_folder = data.get('destination_folder')
    print(f"Destination subfolder: {destination_folder}")

    # Ensure main folder exists
    if not os.path.exists(main_destination_folder):
        os.makedirs(main_destination_folder)

    full_destination_path = os.path.join(main_destination_folder, destination_folder)

    if not os.path.exists(full_destination_path):
        os.makedirs(full_destination_path)

    try:
        shutil.move(source_file, os.path.join(full_destination_path, os.path.basename(source_file)))
        return jsonify({'message': 'File moved successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run Flask in a separate thread
def run_flask():
    app.run(port=8000)


# Start Flask and GUI in separate threads
if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    open_gui()
