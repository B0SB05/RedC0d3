import jwt 


def encode(key,msg,algo=0):
	if algo == 1 : 
		return jwt.encode(msg,key,algorithm='HS256')
	elif algo == 2:
		return jwt.encode(msg,key,algorithm='RS256')
	else:
		return "[!] Which Algorithm ...."

def verifying(key,msg,algo=0):
	if algo == 1 : 
		return jwt.decode(msg,key,algorithm='HS256',verify=True)
	elif algo == 2:
		return jwt.decode(msg,key,algorithm='RS256',verify=True)
	else:
		return "[!] Which Algorithm ...."


def decode(key,msg,algo=0):
	if algo == 1 : 
		return jwt.decode(msg,key,algorithms=['HS256'])
	elif algo == 2:
		return jwt.decode(msg,key,algorithms=['RS256'])
	else:
		return "[!] Which Algorithm ...." 


msg = {'data':'Cool'}
key="secret"
encoded_data=encode(key,msg,1)
#decoded_data= decode(key,encoded_data,1)
print(verifying(key,encoded_data,1))
print(encoded_data)
#print(decoded_data)
