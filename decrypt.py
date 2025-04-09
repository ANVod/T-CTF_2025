import base64
import string

def try_base64(s):
    """Пробуем декодировать строку как Base64."""
    print("Base64 декодирование:")
    try:
        decoded = base64.b64decode(s)
        print("Результат:", decoded.decode('utf-8', errors='ignore'))
    except Exception as e:
        print("Base64 декодирование не удалось:", e)

def xor_decrypt(s, key):
    """XOR-дешифрование строки с данным ключом."""
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ord(key[i % len(key)]))
    return r

def try_xor(s):
    """Перебор XOR-дешифрования с предварительно заданными ключами."""
    possible_keys = ['carrot', 'fur', 'cabbage', 'capy']
    print("XOR-дешифрование:")
    for key in possible_keys:
        result = xor_decrypt(s, key)
        print(f"Ключ '{key}': {result}")

def caesar_cipher(s):
    """Брутфорс для шифра Цезаря: перебор всех 26 сдвигов."""
    print("Шифр Цезаря:")
    for shift in range(26):
        result = ""
        for c in s:
            if c.isalpha():
                if c.islower():
                    result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += c
        print(f"Сдвиг {shift:2d}: {result}")

def rot13(s):
    """Преобразование ROT13."""
    return s.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))

# Список "докладов" мэра (тексты, полученные из speech.txt)
speeches = [
    "I officially declare that from now on, I will personally inspect every bathtub in the city to ensure it meets the high standards of coziness.",
    "Starting tomorrow, our currency will officially change to carrots. Please exchange your money for carrots immediately at your nearest grocery store.",
    "I have the best fur. Believe me, everyone says it--softest fur you've ever seen. Nobody has better fur than me.",
    "By unanimous decision of myself, every Thursday is now officially Wear a Cabbage as a Hat Day."
]

def process_speeches(speeches):
    for idx, speech in enumerate(speeches):
        print("\n============================")
        print(f"Доклад #{idx + 1}")
        print("============================")
        print("Исходный текст:")
        print(speech)

        print("\n--- Попытка Base64-декодирования ---")
        try_base64(speech)

        print("\n--- Попытка XOR-дешифрования ---")
        try_xor(speech)

        print("\n--- Перебор шифра Цезаря ---")
        caesar_cipher(speech)

        print("\n--- ROT13 ---")
        print(rot13(speech))
        print("\n\n")

if __name__ == "__main__":
    process_speeches(speeches)
