from twilio.rest import Client

account_sid = 'AC21b553ae63f9ee2c39f39236f7d3f5f3'
auth_token = 'ac83ec71d4725f168494bb12c64555ca'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+919972910248'
)

print(message.sid)
