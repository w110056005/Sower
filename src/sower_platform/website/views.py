from django.shortcuts import render
from django.http import HttpResponse
import zmq
import subprocess

# Create a ZeroMQ context
context = zmq.Context()
# Create a publisher socket
socket = context.socket(zmq.PUB)
# Bind the publisher socket to a specific address
socket.bind("tcp://0.0.0.0:5555")

def execute_python_file(file_path):
    try:
        # Execute the Python file as a separate process
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the execution
        print(f"Error executing {file_path}: {e}")

# Create your views here.
def hello(request):
    print("Sending...")
    message = "Start"
    socket.send_string(message)
    execute_python_file("./website/server.py")
    return HttpResponse("Hello, world!")

