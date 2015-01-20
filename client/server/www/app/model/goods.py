from app.db import *
from common.phpserialize import *
'''
get goods info
@params goods_id 
@return 
'''
def get_goods_info(goods_id):
    sqlstr = '''SELECT g.*, c.measure_unit, b.brand_id,b.brand_desc,b.brand_logo,
     b.brand_name AS goods_brand,IFNULL(AVG(r.comment_rank), 0) AS comment_rank 
    from %s as g left join %s as c on g.cat_id=c.cat_id left join %s as b on 
     g.brand_id=b.brand_id left join %s as r on r.id_value=g.goods_id and r.comment_type
    = 0 and r.parent_id = 0 and r.status=1 where g.goods_id = %d '''
    sql = sqlstr%(tables['goods'],tables['category'],tables['brand'],tables['comment'],goods_id)
    rs=fetchone(sql)
    return rs
'''
get goods attr
@params goods_id 
@return 
'''
def get_goods_attr(goods_id):
    sqlstr = '''SELECT attrs FROM %s WHERE goods_id=%d'''
    sql = sqlstr%(tables['goods'],goods_id)
    rs=fetchone(sql)
    attrs = loads(rs['attrs'])
    out = []
    for k,v in attrs:
        sql = 'SELECT attr_value from %s where value_id = %d' % (tables['attr_value'],v)
        sql2 = 'SELECT attr_value from %s where value_id = %d' % (tables['attribute'],k)
        rs1 = fetchone(sql)
        rs2 = fetchone(sql2)
        out.append = {'name':rs2['attr_name'],'value':rs1['attr_value']}
    return out
'''
get goods gallery
@params goods_id 
@return 
'''
def get_goods_gallery(goods_id):
    num = 5
    sql = '''SELECT img_id, img_url, thumb_url, img_desc
    FROM %s where goods_id = %d'''%(tables['goods_gallery'],goods_id)
    rs = fetchall(sql)
    return rs 
'''
get goods all
@params goods_id 
@return 
'''
def get_goods_all(goods_id):
    goods_info=get_goods_info
    goods_info['attr'] = get_goods_attr
    goods_info['gallery'] = get_goods_gallery
    return goods_info
