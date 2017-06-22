# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC1a7339529e4074af182f7ce55aa7ac17"
auth_token = "694981e351f9e86d3d908ebdc889ec89"
client = Client(account_sid, auth_token)

queue = client.queues("QU5ef8732a3c49700934481addd5ce1659") \
              .fetch()

print(queue.average_wait_time)
