import base64

encrypted = base64.b64decode(open("encrypted.txt", "rb").read())

# Перебор всех возможных ключей из контекста
for key_candidate in ["carrots", "capy", "fur", "Kapibarovsk"]:
    key = key_candidate.encode()
    decrypted = bytes([encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted))])
try:
    print(f"Key: {key_candidate}")
    print(decrypted.decode())
except:
    print("Ошибка декодирования")