from twilio.rest import Client 
 
account_sid = 'AC144ba0c1b6855587de5157af9a3a46b0' 
auth_token = '971c159f0335a1d41a0057078c3fd4fd' 
client = Client(account_sid, auth_token) 
 
def send_love():
	message = client.messages.create( 
                              	from_='whatsapp:+14155238886',  
                              	body='abhe alok tujhe kuch kaam dhaam to hai nahi aa jaata hai freefire khelne chu hai kya kam phone chalaya kar nahi to maarunga itna hadiyaan tut jaayegi freefire ka naam bhi bhul jaayega.',      
                              	to='whatsapp:+919987128200'
                                        #to='whatsapp:+918454850552'
                          	) 
 
	print(message.sid)