import qrcode

# Safe QR
safe = qrcode.make("https://google.com")
safe.save("safe_qr.png")

# Phishing QR
phish = qrcode.make("http://secure-login-update.com")
phish.save("phishing_qr.png")

print("QR codes generated!")