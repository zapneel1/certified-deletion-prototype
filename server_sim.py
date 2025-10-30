"""
Server (receiver) simulation.
Receives BB84 qubits (as QuantumCircuit) and measures them to produce a deletion certificate.
"""

from bb84 import measure_in_hadamard


def server_measure_and_return_certificate(qc):
    """
    Simulate the receiver measuring all qubits in the Hadamard basis.
    Returns classical bitstring (list[int]) as deletion certificate.
    """
    return measure_in_hadamard(qc)
