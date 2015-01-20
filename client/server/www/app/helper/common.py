from app.db import *

def cook_ext(ext):
    ext_list=ext.split('.')
    out={}
    for v in ext_list:
        val=int(v)
        if val!=0:
            sql = "select attr_id,value_id from %s where value_id=%d"%\
            (tables['attr_value'],val)
            rs=fetchone(sql)
    return out