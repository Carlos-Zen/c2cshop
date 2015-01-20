from app.models import HrUsers as Users
from hashlib import sha1
from common import setting


def check_user_password(username,passwd,call_back=''):
    passwd=encode_password(passwd)
    try:
        data=Users.objects.filter(user_name=username,password=passwd).values('user_id',
        'user_name','email','user_money','user_icon','realname')
    except Users.DoesNotExist:
        return false
    else:
        return data

def encode_password(passwd):
    str=passwd+setting.encryption_key
    sha = sha1()
    sha.update(str)
    return sha.hexdigest()