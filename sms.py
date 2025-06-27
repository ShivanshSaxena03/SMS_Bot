from twilio.rest import Client

account_sid = 'Your_Account_SID'
auth_token = 'Your_Auth_Token'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='Your_Twilio_Number',
  body='Your custom message',
  to='Verified_Recipient_Number'
)

print(message.sid)
