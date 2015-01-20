from app.db import *
from common.phpserialize import *
from app.model.common_model import *


def get_address(user_id,num=6):
    rs=get_data('address',{'user_id':user_id},num)
    return rs

def get_address_info(address_id):
    rs=get_one('address',{'address_id':address_id})
    return rs
def get_shipping_list():
    rs=get_data('shipping')
    return rs

def add_address():
    
    return True

def delete_address(user_id,address_id):
        
    DB.where({'user_id':user_id,'address_id':address_id}).delete(tables['address'])
    return True

def update_address(user_id,address_id,data):
    DB.where('address_id',address_id).update(tables['address'],data)
    return True
