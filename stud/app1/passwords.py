import bcrypt


def Passencrypt(data):
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(data.encode('utf-8'),salt).decode('utf-8')

def Passdecrypt(user_pass,db_pass):
    return bcrypt.checkpw(user_pass.encode('utf-8'),db_pass.encode('utf-8'))