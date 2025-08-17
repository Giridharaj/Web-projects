# First, you need to install Flask and the Qiskit packages if you haven't already:
# pip install Flask qiskit qiskit-aer

from flask import Flask, jsonify, request
from qiskit import QuantumCircuit, Aer, execute, transpile, assemble

# Create a Flask application instance.
app = Flask(__name__)

# --- Qiskit Circuit Logic ---
# This function defines and runs a simple quantum circuit.
# In this example, it creates a Bell state |00> + |11>.
def run_bell_state_circuit(shots):
    """
    Creates and executes a Bell state quantum circuit on a local simulator.
    Args:
        shots (int): The number of times to run the circuit.
    Returns:
        dict: The measurement counts from the circuit execution.
    """
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Apply a Hadamard gate to the first qubit (q0) to put it in a superposition.
    qc.h(0)
    
    # Apply a CNOT gate with q0 as the control and q1 as the target.
    # This entangles the two qubits.
    qc.cx(0, 1)
    
    # Measure both qubits and map the results to the classical bits.
    qc.measure([0, 1], [0, 1])
    
    # Select the local Qiskit Aer simulator for execution.
    backend = Aer.get_backend('qasm_simulator')
    
    # Transpile and assemble the circuit for the simulator.
    compiled_circuit = transpile(qc, backend)
    qobj = assemble(compiled_circuit, shots=shots)

    # Execute the circuit and get the job result.
    job = backend.run(qobj)
    result = job.result()
    
    # Return the measurement counts.
    return result.get_counts()

# --- Flask API Endpoint ---
# This is the API endpoint that the front-end will call.
# The route is '/run-circuit' and it accepts POST requests.
@app.route('/run-circuit', methods=['POST'])
def run_circuit_api():
    """
    API endpoint to run the quantum circuit.
    Expects a JSON payload with a 'shots' key.
    """
    # Check if the incoming request has JSON data.
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get the JSON data from the request body.
    data = request.get_json()
    
    # Extract the 'shots' parameter from the request. Use a default if not provided.
    shots = data.get('shots', 1024)
    
    # Ensure shots is an integer.
    try:
        shots = int(shots)
    except (ValueError, TypeError):
        return jsonify({"error": "Shots must be a number"}), 400

    print(f"Running quantum circuit with {shots} shots...")
    
    try:
        # Call the Qiskit function to execute the circuit.
        counts = run_bell_state_circuit(shots)
        
        # Return the results as a JSON response.
        return jsonify({
            "message": "Quantum circuit executed successfully.",
            "results": counts
        })
    except Exception as e:
        # Handle any errors during Qiskit execution.
        return jsonify({"error": str(e)}), 500

# To run the API, use the following command in your terminal:
# python your_file_name.py
# If you are using a development server, you can use:
# flask run
# This line is for running the app directly in this script.
if __name__ == '__main__':
    # 'debug=True' reloads the server automatically on code changes.
    app.run(debug=True)
