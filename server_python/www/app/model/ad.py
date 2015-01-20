from app.db import *
from common.phpserialize import *

def get_cat_ad(cat_id):
    rs=DB.select('*').fm(tables['ad']).where({'enabled':1,'media_type':0,'cat_id':cat_id})\
    .order('sort_order','desc').all()
    return rs


    

