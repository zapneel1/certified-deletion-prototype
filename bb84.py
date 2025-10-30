from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def prepare_bb84_circuit(x_bits, theta_bits):
    n = len(x_bits)
    qc = QuantumCircuit(n, n)
    for i in range(n):
        if x_bits[i] == 1:
            qc.x(i)
        if theta_bits[i] == 1:
            qc.h(i)
    return qc

def measure_in_hadamard(qc):
    n = qc.num_qubits
    qc.barrier()
    for i in range(n):
        qc.h(i)
        qc.measure(i, i)
    backend = Aer.get_backend('aer_simulator')
    job = execute(qc, backend=backend, shots=1)
    counts = job.result().get_counts()
    bitstring = list(counts.keys())[0][::-1]
    return [int(b) for b in bitstring]

def random_bits(n, seed=None):
    rng = np.random.RandomState(seed)
    return [int(b) for b in rng.randint(0, 2, size=n)]
