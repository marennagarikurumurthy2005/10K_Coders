import bcrypt

def paw_hashing(input_pasword):
    salt=bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(input_pasword.encode('utf-8'),salt).decode('utf-8')

