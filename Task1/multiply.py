"""
QOSF Cohort 6 Task 1 Screening
Author: Arkaprava Choudhury

This file is a last-ditch attempt to code the multiplier in Qiskit.
I am much more familiar with Tequila than Qiskit, so that explains why this is a bare skeleton of code.
"""
import tequila as tq
import numpy as np
from numpy import pi, floor, log2
from numpy import binary_repr as binrep
import qiskit

from qiskit import QuantumCircuit, transpile, assemble, Aer, IBMQ
from qiskit.circuit.quantumcircuitdata import CircuitInstruction
from qiskit.tools.monitor import job_monitor


def multiplier(num1: int, num2: int, verbose: bool = False):
    """

    """
    # initialize variables
    bin1, bin2 = binrep(num1), binrep(num2)
    n1_bits, n2_bits = int(floor(log2(num1) + 1)), int(floor(log2(num2) + 1))
    m = max(n1_bits, n2_bits)
    bin1, bin2 = '0' * (m - n1_bits) + bin1, '0' * (m - n2_bits) + bin2
    n_bits, n1_bits, n2_bits = 2 * m, m, m
    if verbose:
        print(bin1, bin2)

    circ = QuantumCircuit(2 * n_bits + 1, n_bits + 1)

    ####
    # Bit encoding
    ####
    for i in range(n1_bits):
        if bin1[i] == "1":
            circ.x(qubit=i)
        if bin2[i] == "1":
            circ.x(qubit=n1_bits+i)

    ####
    # QFT
    ####
    # QFT Rotations
    for i in range(n_bits):
        if verbose:
            print("H on ", 2 * n_bits - i)
        circ.h(qubit=2*n_bits-i)
        for c in range(n_bits - i - 1):
            if verbose:
                print("CP on ", n_bits + i, " with control ", c)
            circ.cp(theta=pi/(2**(c-1)), control_qubit=n_bits+c, target_qubit=2*n_bits-i)
    circ.h(qubit=n_bits)
    # QFT Swaps
    for i in range(n_bits // 2):
        if verbose:
            print("Swap between ", n_bits + i, " and ", 2 * n_bits - i - 1)
        circ.swap(n_bits + i, 2 * n_bits - i - 1)

    ####
    # Controlled rotations
    ####
    for i in range(n1_bits):
        print(i)
        ...

    for i in range(n1_bits):
        for j in range(n2_bits):
            ...

    return 0


def qft(circuit: QuantumCircuit, n: int):
    """
    Input:
        - n is the number of qubits
    """
    _qft_rotations(circuit, n)
    _swap_registers(circuit, n)
    return circuit


def _qft_rotations(circuit, n):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)
    # At the end of our function, we call the same function again on
    # the next qubits (we reduced n by one earlier in the function)
    _qft_rotations(circuit, n)


def _swap_registers(circuit, n):
    for qubit in range(n // 2):
        circuit.swap(qubit, n - qubit - 1)
    return circuit


def adder():
    pass


if __name__ == "__main__":
    # Let's see how it looks:
    qc = QuantumCircuit(4)
    qft(qc, 4)
    qc.draw()
    multiplier(2, 2, True)
