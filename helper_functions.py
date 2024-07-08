import re
import os
from werkzeug.utils import secure_filename
from app import app

def convert_to_float(s):
    numbers = re.findall(r'\d+', s)
    if numbers:
        return float(numbers[0])
    return 0.0

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def ensure_upload_folder_exists():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
