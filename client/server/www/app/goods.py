from app.models import HrGoods as Goods
from django.db import connection
db_pre = 'hr_'
def get_goods_info(goods_id):
    sqlstr = '''SELECT g.*, c.measure_unit, b.brand_id,b.brand_desc,b.brand_logo,
     b.brand_name AS goods_brand,IFNULL(AVG(r.comment_rank), 0) AS comment_rank 
    from %s as g left join %s as c on g.cat_id=c.cat_id left join %s as b on 
     g.brand_id=b.brand_id left join %s as r on r.id_value=g.goods_id and r.comment_type
    = 0 and r.parent_id = 0 and r.status=1 where g.goods_id = %d '''
    sql = sqlstr%(db_pre+'goods',db_pre+\
    'category',db_pre+'brand',db_pre+'comment',goods_id)
    print(sql)
    cur = connection.cursor()
    cur.execute(sql)
    rs=cur.fetchone()
    return rs