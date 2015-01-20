from django.db import connection
cursor = connection.cursor()
'''
Simple function for one result sql
'''

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