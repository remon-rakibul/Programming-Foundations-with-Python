from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1f7871f2eec613f8242ab63b8fb9fbab"
# Your Auth Token from twilio.com/console
auth_token  = "376565e0f76a5d371ec710f2e151dc8d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8801711309969", 
    from_="+17073685759",
    body="Hello from Evanka Trump!")

print(message.sid)
