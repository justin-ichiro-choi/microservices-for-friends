import subprocess
import sys
import time
import json

try:
    import zmq
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyzmq"])


# Code begins
# --------------------------------------------------------------------- #


# Can make a call to microservice using make_query (with a search phrase)
def make_query(search_phrase):

    #  Socket setup to talk to server
    context = zmq.Context()

    print("Establishing connection")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")

    # Send phrase to search Google Results
    socket.send_string(search_phrase)

    #  Get the reply.
    message = json.loads(socket.recv())
    print("Received list of 10 results for %s" % (search_phrase))

    return message