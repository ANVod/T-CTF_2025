import base64

encrypted = base64.b64decode(open("encrypted.txt", "rb").read())
key = "capybara".encode() # 8 байт (название города [[3]])

decrypted = bytes([encrypted[i] ^ key[i % 8] for i in range(len(encrypted))])
print(decrypted.decode("latin-1"))