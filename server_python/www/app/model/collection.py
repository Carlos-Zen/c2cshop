from app.db import *
from common.phpserialize import *
from app.model.common_model import *

def get_collect_list(user_id, cat_id, size = 100, page = 1):
    return get_data('collect',{'user_id':user_id},size,page)

def get_collect_num(user_id, cat_id):
    return get_count('collect',{'user_id':user_id})

def add_collect(user_id,goods_id):
    num=get_count('collect',{'user_id':user_id,'goods_id':goods_id})
    if int(num) > 0:
        return 'has been added'
    else:
        DB.insert(tables['collect'],{'user_id':user_id,'goods_id':goods_id})
    return True

def cancel_collect(user_id,rec_id):
    
    DB.where({'user_id':user_id,'rec_id':rec_id}).delete(tables['collect'])
    return True
        