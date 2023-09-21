import random

def quantum_teleportation():
    print("Welcome to Quantum Odyssey - Teleportation Challenge!")
    print("You are a quantum scientist trying to teleport a qubit to a distant location.")
    print("You have a quantum entangled pair of qubits and need to apply gates to teleport your qubit.")
    print("Your goal is to ensure the distant qubit matches the original qubit state.")

    original_qubit = random.choice([0, 1])  # Random initial state (0 or 1)
    entangled_pair = [random.choice([0, 1]), None]  # Initialize entangled pair with one unknown state

    print(f"Your original qubit: |{original_qubit}>")
    print(f"Entangled pair: |{entangled_pair[0]}> and |? (unknown)>")

    while entangled_pair[1] is None:
        print("\nChoose an operation:")
        print("1. Apply X Gate")
        print("2. Apply Z Gate")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Apply X gate (bit flip)
            entangled_pair[1] = (entangled_pair[0] + 1) % 2
        elif choice == '2':
            # Apply Z gate (phase flip)
            entangled_pair[1] = entangled_pair[0]
        else:
            print("Invalid choice. Please select 1 or 2.")

    print("\nTeleportation complete!")
    print(f"Original qubit: |{original_qubit}>")
    print(f"Teleported qubit: |{entangled_pair[1]}>")

    if original_qubit == entangled_pair[1]:
        print("Congratulations! You successfully teleported the qubit.")
    else:
        print("Teleportation failed. The qubits do not match.")

if __name__ == "__main__":
    quantum_teleportation()
