from app.db import *
from common.phpserialize import *
from app.helper.common import cook_ext
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
Get category goods ,used for goods category pages
@params cat_id
@params brand Brand id for filter
@params min  Min price for filter
@params max 
@params ext
@params size
@params page
@params order
@params desc
@return List
'''
def get_category_goods(cat_id,brand = 0, min = 0, max = 0, ext\
     = '0.0.0.0', size = 10, page = 1, order, desc = 1):
        if order in ['click_count', 'discount', 'salesvol', 'add_time', 'salesvol']:
            if desc==1:
                order_str=''.join([order,' DESC'])
            else:
                order_str=order
        else:        
            order_str=order
        ext_list = cook_ext(ext)
        
        where='''g.cat_id=%d AND g.is_on_sale = 1
         AND g.is_alone_sale = 1 AND g.is_delete = 0 '''%(cat_id)
    