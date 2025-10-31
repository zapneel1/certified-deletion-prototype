# Certified Deletion Prototype (Quantum Cryptography Demo)

This repository implements a **prototype of the "Cryptography with Certified Deletion"** concept from the paper  
> *Garg, Yuen, et al. (2022). Cryptography with Certified Deletion*.

---

## What is Certified Deletion?

Normally, when someone receives encrypted data, they can **store and decrypt it later**.  
But quantum mechanics changes the game — measuring a quantum state *irreversibly destroys information*.  

Certified deletion uses this principle to build an **encryption system where deletion can be verified**.

### Core Idea
When Alice encrypts a bit `b` for Bob:
1. She generates random bitstrings `x` and `θ`.  
2. She encodes each bit of `x` in the basis given by `θ`:  
   - If `θᵢ=0`: use computational basis |0⟩/|1⟩  
   - If `θᵢ=1`: use Hadamard basis |+⟩/|−⟩  
3. The resulting **BB84 qubits** `|x⟩_θ` form the *quantum ciphertext*.
4. She masks `b` by XORing it with the parity of some bits of `x`, then encrypts that with a standard (classical) cipher.

To **certify deletion**, Bob must:
- Measure all qubits in the Hadamard basis, producing outcomes `x′`.
- Send `x′` to Alice as a *deletion certificate*.

Alice verifies:
> For all indices where θᵢ=1, x′ᵢ == xᵢ.  

If true → the qubits were destroyed, and `b` can no longer be recovered.

---

## Implementation Overview

This repo implements a **simulated version** of the scheme using Python and [Qiskit](https://qiskit.org/).

### Components

| File | Description |
|------|--------------|
| `src/bb84.py` | Prepares BB84 states and simulates measurement. |
| `src/classical_crypto.py` | Simple AES-based encryption (placeholder for PQ crypto). |
| `src/compiler.py` | High-level certified-deletion compiler (encrypt, delete, verify). |
| `src/server_sim.py` | Simulated receiver measuring and returning certificate. |
| `src/adversary_sim.py` | Cheating strategies (Z-basis, partial, etc.). |
| `src/tests/test_honest_flow.py` | Honest end-to-end test (should pass). |
| `src/tests/test_cheat_strategies.py` | Cheating runs (should mostly fail). |

---

## 🧰 Requirements

```bash
pip install -r requirements.txt
