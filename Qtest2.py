from qiskit import *
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
#matplotlib inline
circuit.draw()