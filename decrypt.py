import base64

encrypted = base64.b64decode(open("encrypted.txt", "rb").read())
key = "carrots".encode()  # Ключ из контекста задачи [[2]]

decrypted = bytes([encrypted[i] ^ key[i % 7] for i in range(len(encrypted))])
print(decrypted.decode("latin-1"))