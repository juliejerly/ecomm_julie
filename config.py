# config.py
BASE_URL = "http://127.0.0.1:5000"
LOGIN_URL = "http://127.0.0.1:5000/login"

VALID_CREDS = {
    "username" : "admin",
    "password" : "admin123"
}

INVALID_CREDS = {
    "username" : "admin1",
    "password" : "admin123"
}
URLS = {
    "text_box": f"{BASE_URL}/text-box",
    "checkbox": f"{BASE_URL}/checkbox",
    "buttons": f"{BASE_URL}/buttons"
}
