# Example of importing function to use in web application. MAKE SURE SERVER IS ACTIVATED (python server.py)

from client import *

# Example: Call client.py to run OR import module and call make query
test = make_query("Excellent cardio exercises for short on time")

# Return value of function will be lists of 10 dictionaries marking top 10 hits from a google search with search phrase
# 3 fields in dictionary: URL, Title, and Description
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

