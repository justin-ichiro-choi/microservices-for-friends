import subprocess
import sys
import time
import json

# Will import needed modules not system defaulted if not available. 
try:
    from googlesearch import *
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "googlesearch-python"])

try:
    import zmq
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyzmq"])

# Converting objects to dictionary (weird, but works?)
class SearchResultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SearchResult):
            return obj.__dict__  # or customize with a specific dictionary
        return super().default(obj)
    
# Setting up socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")

print("Spinning up Server")



# Usage


# Receiver
while True:
    message = socket.recv()
    print("Received request to collate resources for: %s" %message)

    data = list(search(message, advanced=True, num_results=10))

    # Gets search results and converts to list for JSONification
    json_string = json.dumps(data, cls=SearchResultEncoder)

    # Sends out data
    socket.send_string(json_string)
