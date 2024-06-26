import subprocess
import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the executable (assuming it is in the same directory)
executable_path = os.path.join(current_directory, 'your_executable.exe')

# Execute the executable and capture its output
result = subprocess.run([executable_path], capture_output=True, text=True)

# Save the output to a variable
output = result.stdout

# Print the output (for demonstration purposes)
print(output)
