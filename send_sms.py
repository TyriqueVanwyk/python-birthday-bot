from twilio.rest import Client 
 
account_sid = 'ACc057ab3c92cf4e70e48f1a206944378d' 
auth_token = 'be9a68a0f844e99a3d25030cc589525e' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+27627004903' 
                          ) 
 
print(message.sid)
