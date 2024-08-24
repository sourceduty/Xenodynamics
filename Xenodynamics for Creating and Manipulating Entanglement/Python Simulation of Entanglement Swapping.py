# Xenodynamics for Creating and Manipulating Entanglement
# Python Simulation of Entanglement Swapping

import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Define a function to create a Bell state
def create_bell_state(qc, qubit1, qubit2):
    qc.h(qubit1)  # Apply Hadamard gate
    qc.cx(qubit1, qubit2)  # Apply CNOT gate

# Initialize quantum circuit with 4 qubits for A1, A2, B1, B2
qc = QuantumCircuit(4)

# Create entangled pair A (A1, A2)
create_bell_state(qc, 0, 1)

# Create entangled pair B (B1, B2)
create_bell_state(qc, 2, 3)

# Perform Bell state measurement on A2 (qubit 1) and B1 (qubit 2)
qc.cx(1, 2)
qc.h(1)
qc.measure_all()

# Simulate the circuit
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts(qc)

# Output the measurement results
counts
