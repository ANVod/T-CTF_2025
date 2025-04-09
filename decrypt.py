key = "Kapi".encode()
decrypted = bytes([encrypted[i] ^ key[i % 4] for i in range(len(encrypted))])
