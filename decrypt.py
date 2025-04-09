# Перебор однобайтовых ключей
encrypted = base64.b64decode(open("encrypted.txt", "rb").read())
for key in range(256):
    try:
        decrypted = bytes([b ^ key for b in encrypted])
        print(f"Key {key}: {decrypted.decode()}")
    except:
        continue