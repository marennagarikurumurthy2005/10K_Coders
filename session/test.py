import bcrypt
import jwt
from datetime import datetime,timezone,timedelta
secret_key = 'kurumurthy@200579892075722s11a6724'
payload_data = {
    'name':'Kurumurthy',
    'age':21,
    'village':'nirven'
}
encode_data = jwt.encode(payload=payload_data,key=secret_key,algorithm='HS256')
print(encode_data)
decode_data = jwt.decode(encode_data,key=secret_key,algorithms='HS256')
print(decode_data)