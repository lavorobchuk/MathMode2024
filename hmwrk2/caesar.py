import typing as tp


def encrypt_caesar(plaintext: str, shift: int) -> str:
    abc_l = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_abc_l = abc_l[shift:] + abc_l[:shift]
    caesar_cipher_l = str.maketrans(abc_l, encrypted_abc_l)

    abc_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_abc_u = abc_u[shift:] + abc_u[:shift]
    caesar_cipher_u = str.maketrans(abc_u, encrypted_abc_u)

    caesar_cipher = {**caesar_cipher_l, **caesar_cipher_u}
    ciphertext = plaintext.translate(caesar_cipher)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    abc_l = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_abc_l = abc_l[shift:] + abc_l[:shift]
    caesar_decipher_l = str.maketrans(encrypted_abc_l, abc_l)

    abc_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_abc_u = abc_u[shift:] + abc_u[:shift]
    caesar_decipher_u = str.maketrans(encrypted_abc_u, abc_u)

    caesar_decipher = {**caesar_decipher_l, **caesar_decipher_u}
    plaintext = ciphertext.translate(caesar_decipher)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
