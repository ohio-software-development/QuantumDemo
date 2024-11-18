from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply gates
qc.h(0) # hadamard gate
qc.cx(0,1) # Controlled not gate

# Measure the qubits
qc.measure([0, 1], [0, 1])
# Visualize the circuit
print(qc)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')  
result = execute(qc, backend=simulator, shots=1024).result()

# Get and print the results
counts = result.get_counts(qc)
print("Counts:", counts)