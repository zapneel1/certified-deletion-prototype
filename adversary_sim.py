"""
Adversary simulation strategies.
Implements cheating strategies for testing Certified Deletion.
"""

from qiskit import QuantumCircuit, Aer, execute


def measure_in_z_basis(qc):
    """Measure all qubits in the computational (Z) basis."""
    n = qc.num_qubits
    qc.barrier()
    for i in range(n):
        qc.measure(i, i)
    backend = Aer.get_backend('aer_simulator')
    job = execute(qc, backend=backend, shots=1)
    bitstring = list(job.result().get_counts().keys())[0][::-1]
    return [int(b) for b in bitstring]


def partial_hadamard_measurement(qc, fraction=0.5):
    """
    Measure a random subset of qubits in Hadamard basis and rest in Z basis.
    fraction = proportion of qubits to measure in Hadamard basis.
    """
    import random
    n = qc.num_qubits
    indices_h = set(random.sample(range(n), int(fraction * n)))

    qc.barrier()
    for i in range(n):
        if i in indices_h:
            qc.h(i)
        qc.measure(i, i)

    backend = Aer.get_backend('aer_simulator')
    job = execute(qc, backend=backend, shots=1)
    bitstring = list(job.result().get_counts().keys())[0][::-1]
    return [int(b) for b in bitstring]
