import jwt
import datetime

with open('jwt.secret', 'r') as jwt_secret:
	SECRET_KEY = jwt_secret.read().strip()

def create(user, email):
	token = {
		'email': email,
		'user': user,
		'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
	}
	cookie = jwt.encode(token, SECRET_KEY, algorithm='HS256')
	return cookie


def decode(token):
	try:
		cookie = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
	except jwt.InvalidAlgorithmError:
		cookie = jwt.decode(token, options={"verify_signature": False}, algorithms=['None'])
	except Exception:
		return None
	return cookie
	
def extract(token, field):
	return token[field]
			
