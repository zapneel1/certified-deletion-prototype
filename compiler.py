"""
High-level Certified Deletion compiler.
Implements encrypt → delete → verify flow for 1-bit messages.
"""

from bb84 import prepare_bb84_circuit, random_bits
from classical_crypto import aes_encrypt_bytes, aes_decrypt_bytes, derive_key_from_password


def encrypt_with_certified_deletion(b: int, n_qubits: int = 64, password: str = "testpw"):
    """
    Encrypt a 1-bit message b using BB84 states and AES as a classical wrapper.
    Returns dict with qubits, ciphertext, and secret data for verification.
    """
    x = random_bits(n_qubits)
    theta = random_bits(n_qubits)

    # parity over indices where theta == 0
    parity = 0
    for i, th in enumerate(theta):
        if th == 0:
            parity ^= x[i]
    bprime = b ^ parity

    # Classical AES encryption of b'
    key = derive_key_from_password(password)
    ciphertext = aes_encrypt_bytes(key, bytes([bprime]))

    # Prepare quantum circuit with BB84 states
    qc = prepare_bb84_circuit(x, theta)

    return {
        "quantum_circuit": qc,
        "ciphertext": ciphertext,
        "x": x,
        "theta": theta,
    }


def verify_deletion(x_original, theta, certificate_xprime):
    """Check that x' matches x on indices where theta==1."""
    for i, th in enumerate(theta):
        if th == 1 and certificate_xprime[i] != x_original[i]:
            return False
    return True


def decrypt_after_accept(ciphertext, x, theta, password="testpw"):
    """Decrypt classical ciphertext and reconstruct original bit b."""
    key = derive_key_from_password(password)
    bprime = aes_decrypt_bytes(key, ciphertext)[0]

    parity = 0
    for i, th in enumerate(theta):
        if th == 0:
            parity ^= x[i]

    b = bprime ^ parity
    return b
