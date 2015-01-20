from app.db import *

def get_data(table,querys={},size=10,page=1):
    DB.select('*').fm(tables[table]).where(querys).limit(size*(page-1),size)
    rs = DB.all()
    return rs
def get_count(table,querys={}):
    DB.select('count(*) as num').fm(tables[table]).where(querys)
    rs = DB.get()
    return rs['num']
def get_one(table,querys={}):
    DB.select('*').fm(tables[table]).where(querys)
    rs = DB.one()
    return rs