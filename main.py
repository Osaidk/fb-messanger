
from fbchat import Client
from fbchat.models import *
import pickle
import login

client = login.run()

# Replace with the name of the friend you want to send the message to
friend_name = input('Enter user name: ')

# Get the user ID of the friend you want to send the message to
users = client.searchForUsers(friend_name)
friend = users[0]

# Replace with the message you want to send
message = input('Enter message here: ')

# Send the message to the friend
sent = client.send(Message(text=message), thread_id=friend.uid, thread_type=ThreadType.USER)

if sent:
    print('Message sent successfully!')

# Disconnect the client
client.logout()
