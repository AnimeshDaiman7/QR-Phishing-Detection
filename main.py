import cv2
import pickle
from feature_extraction import extract_features
import requests

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Load QR image (MAKE SURE NAME IS CORRECT)
img = cv2.imread(r"C:\Users\Anime\Desktop\QR_Phishing_Detection\test_qr.png")

# Safety check
if img is None:
    print("❌ Error: Image not found. Check filename/path.")
    exit()

# QR detection
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

print("🔍 Extracted URL:", data)

# If no QR detected
if not data:
    print("❌ No QR code detected")
    exit()

# 🔁 Redirection handling (QsecR concept)
try:
    response = requests.get(data, allow_redirects=True, timeout=5)
    final_url = response.url
    print("🔗 Final URL after redirection:", final_url)
except:
    final_url = data

# Extract features
features = extract_features(final_url)

# Predict
result = model.predict([features])

print("\n===== RESULT =====")
if result[0] == 1:
    print("⚠️ Phishing Website Detected!")
else:
    print("✅ Safe Website")