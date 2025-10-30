"""
Simple AES-based classical encryption for prototype use only.
Replace with a real post-quantum primitive (e.g., Kyber + AES) for production.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib


def derive_key_from_password(password: str) -> bytes:
    """Derive 256-bit AES key from password (SHA-256)."""
    return hashlib.sha256(password.encode()).digest()


def aes_encrypt_bytes(key_bytes: bytes, plaintext_bytes: bytes) -> bytes:
    """AES-CBC encrypt bytes with PKCS7 padding."""
    iv = get_random_bytes(16)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext_bytes, 16))
    return iv + ct


def aes_decrypt_bytes(key_bytes: bytes, ciphertext: bytes) -> bytes:
    """AES-CBC decrypt bytes with PKCS7 unpadding."""
    iv, ct = ciphertext[:16], ciphertext[16:]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), 16)
    return pt
