def encrypt_vigenere(text: str, key: str) -> str:
    encrypted_text = ""
    key_index = 0
    for symbol in text:
        key_shift = ord(key[key_index % len(key)].lower()) - ord('a')
        if symbol.isalpha():
            if symbol.isupper():
                encrypted_symbol = chr((ord(symbol) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                encrypted_symbol = chr((ord(symbol) - ord('a') + key_shift) % 26 + ord('a'))
            encrypted_text += encrypted_symbol
        else:
            encrypted_text += symbol
        key_index += 1
    return encrypted_text


def decrypt_vigenere(encrypted_text: str, key: str) -> str:
    decrypted_text = ""
    key_index = 0
    for symbol in encrypted_text:
        key_shift = ord(key[key_index % len(key)].lower()) - ord('a')
        if symbol.isalpha():
            if symbol.isupper():
                decrypted_symbol = chr((ord(symbol) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                decrypted_symbol = chr((ord(symbol) - ord('a') - key_shift) % 26 + ord('a'))
            decrypted_text += decrypted_symbol
        else:
            decrypted_text += symbol
        key_index += 1
    return decrypted_text

