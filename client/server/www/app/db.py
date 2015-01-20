from django.db import connection
db_pre = 'hr_'
tables = {}
tables['goods'] = ''.join([db_pre,'goods'])
tables['attr_value'] = ''.join([db_pre,'attr_value'])
tables['attribute'] = ''.join([db_pre,'attribute'])
tables['attrs'] = db_pre,'goods'
tables['brand'] = ''.join([db_pre,'brand'])
tables['comment'] = ''.join([db_pre,'comment'])
tables['category'] = ''.join([db_pre,'category'])
tables['goods_gallery'] = ''.join([db_pre,'goods_gallery'])
cursor = connection.cursor()


def fetchone(sql):
    cursor.execute(sql)
    try:
        col_names = [row[0] for row in cursor.description]
        rs = dict(zip(col_names,cursor.fetchone()))        
    except:
        rs = {}    
          
    return rs

def fetchall(sql):
    cursor.execute(sql)
    try:
        col_names = [row[0] for row in cursor.description]
        data = cursor.fetchall()
        rs = [dict(zip(col_names,raw)) for raw in data]
    except:
        rs=[]
    return rs