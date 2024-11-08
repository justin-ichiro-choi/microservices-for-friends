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


# Example: Call client.py to run OR import module and call make query
test = make_query("Excellent cardio exercises for short on time")

# Return value of function will be lists of 10 dictionaries marking top 10 hits from a google search with search phrase
# 3 fields in dictionary: URL, Title, and Dictionary
for entry in test: 
    print("")
    print(entry['url'])
    print(entry['title'])
    print(entry['description'])
    print("")

# To get a specific entry (i.e, top search result),
print(test[0])

# And for a specific information for an entry

print(test[0]['url'])
print(test[0]['title'])
print(test[0]['description'])

