from twilio.rest import Client 
 
account_sid = 'AC144ba0c1b6855587de5157af9a3a46b0' 
auth_token = '971c159f0335a1d41a0057078c3fd4fd' 
client = Client(account_sid, auth_token) 
 
def send_love():
	message = client.messages.create( 
                              	from_='whatsapp:+14155238886',  
                              	body='Alok tu Chu  Hain aur tu Nob hain.',      
                              	to='whatsapp:+919987128200'
                                        #to='whatsapp:+918454850552'
                          	) 
 
	print(message.sid)