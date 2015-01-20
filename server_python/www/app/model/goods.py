from app.db import *
from common.phpserialize import *
from time import *
from app.model.common_model import *
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
    for k in attrs.keys():
        try:
            sql = 'SELECT attr_value from %s where value_id = %d' % (tables['attr_value'],int(attrs[k]))
            sql2 = 'SELECT attr_name from %s where attr_id = %d' % (tables['attribute'],k)
            rs1 = fetchone(sql)
            rs2 = fetchone(sql2)
            out.append({'name':rs2['attr_name'],'value':rs1['attr_value']})
        except:
            pass
    return out

'''
get goods buy selector attr
@params goods_id 
@return 
'''
def get_goods_battr(goods_id):
    
    rs=DB.select('goods_attr_id,attr_id,attr_value,attr_name,is_pic').fm(tables['goods_attr']).where('goods_id',goods_id)\
    .order('sort_order').all()
    out = {}
    for item in rs:
        try:
            if isinstance(out[item['attr_id']],dict):
                additm={'goods_attr_id':item['goods_attr_id'],'attr_value':item['attr_value']}
                out[item['attr_id']]['attrs'].append(additm)    
        except:
            additm = {'attr_id':item['attr_id'],'attr_name':item['attr_name'],'is_pic':item['is_pic'],'attrs':[]}
            additm['attrs'].append({'goods_attr_id':item['goods_attr_id'],'attr_value':item['attr_value']})
            out[item['attr_id']]=additm
    final_data = []
    for key in out.keys():
        final_data.append([key,out[key]])
    return final_data  
    


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
    goods_info=get_goods_info()
    goods_info['attr'] = get_goods_attr()
    goods_info['gallery'] = get_goods_gallery()
    return goods_info

'''
get group,special,
'''
def get_various_goods(type,cat_id=0,size=10,page=1,order='sort_order',desc=1):   
    '''
    Get category goods ,used for goods category pages
    '''
    if order in ['click_count', 'discount', 'salesvol', 'add_time', 'salesvol']:
        if desc==1:
            DB.order(order,'desc')
        else:
            DB.order(order)
    else:        
        DB.order('sort_order')
    

    select_fields = '''goods_id, goods_name,market_price, shop_price,
    attrs,discount,salesvol,promote_price, promote_start_date, promote_end_date,
     goods_brief, goods_thumb, goods_img,seller_id'''
    DB.select(select_fields)
    

    DB.where('cat_id',cat_id)
    
    if isinstance(type, str):
        DB.where('is_%s'%type,1)
    
    DB.fm(tables['goods']).limit(size*(page-1),size)
    
    goods=DB.all()

    return goods

'''
get group,special,  number
'''
def get_various_num(type,cat_id=0):   
    '''
    Get category goods number,used for goods category pages 
    '''
    DB.select('count(*) as num')
    

    DB.where('cat_id',cat_id)
    
    if isinstance(type, str):
        DB.where('is_%s'%type,1)
    
    DB.fm(tables['goods'])
    
    rs=DB.all()

    return rs


'''
get special brand good activity list
'''
def get_special_actlist(cat_id=0,size=10,page=1,condition='on'):
    type=2
    if int(cat_id)>0:
        DB.where('g.cat_id',cat_id)
    now=time()
    if condition == 'on':
        DB.where('bc.end_time>',now)
    elif condition == 'to':
        DB.where('bc.start_time>',now)
    DB.select('bc.*,b.brand_id').fm(''.join([tables['brand_activity'],' as bc ']))\
    .join(''.join([tables['brand'],' as b ']),'b.brand_id = bc.brand_id').where('bc.act_type',type)\
    .where('bc.status',1).order('bc.sort_order').limit(size*(page-1),size)
    rs = DB.all()

    for i in range(len(rs)):
        stime = localtime(rs[i]['start_time'])
        start_time = strftime('%Y-%m-%d %H:%M',stime)
        etime = localtime(rs[i]['end_time'])
        end_time = strftime('%Y-%m-%d %H:%M',etime)
        rs[i]['formated_start_date'] = start_time
        rs[i]['formated_end_date'] = end_time       
    return rs

def act_special_actnum(cat_id=0,condition='on'):
    type=2
    if int(cat_id)>0:
        DB.where('g.cat_id',cat_id)
    now=time()
    if condition == 'on':
        DB.where('bc.end_time>',now)
    elif condition == 'to':
        DB.where('bc.start_time>',now)
    DB.select('count(*) as num').fm(''.join([tables['brand_activity'],' as bc ']))\
    .join(''.join([tables['brand'],' as b ']),'b.brand_id = bc.brand_id').where('bc.act_type',type)\
    .where('bc.status',1)
    rs = DB.get()   
    return rs['num']

def get_special_glist(cat_id=0,brand_id,size=10,page=1,order='sort_order',desc=1):
    if order in ['click_count', 'discount', 'salesvol', 'add_time', 'salesvol']:
        if desc==1:
            DB.order(order,'desc')
        else:
            DB.order(order)
    else:        
        DB.order('sort_order')
    

    select_fields = '''b.*, IFNULL(g.goods_thumb, '') AS goods_thumb,g.cat_id,g.shop_price ,g.brand_id,
    g.promote_price,g.discount,g.salesvol,b.start_time AS start_date, b.end_time AS end_date '''
    DB.select(select_fields).fm(''.join([tables['goods_activity'],' as b ']))\
    .join(''.join([tables['goods'],' as g ']),'b.goods_id = g.goods_id').where({'brand_id':brand_id,'cat_id':cat_id})\
    .order('bc.sort_order').limit(size*(page-1),size)
    rs = DB.all()
    
    return rs


def get_sec_desc():
    sqlstr = '''SELECT g.*, c.measure_unit, b.brand_id,b.brand_desc,b.brand_logo,
     b.brand_name AS goods_brand,IFNULL(AVG(r.comment_rank), 0) AS comment_rank 
    from %s as g left join %s as c on g.cat_id=c.cat_id left join %s as b on 
     g.brand_id=b.brand_id left join %s as r on r.id_value=g.goods_id and r.comment_type
    = 0 and r.parent_id = 0 and r.status=1 where g.is_killer = 1 '''
    sql = sqlstr%(tables['goods'],tables['category'],tables['brand'],tables['comment'])
    rs=fetchone(sql)
    return rs
def get_sec_info():
    '''
    Second kill goods  info
    '''
    sqlstr = '''SELECT g.*, c.measure_unit, b.brand_id,b.brand_desc,b.brand_logo,
     b.brand_name AS goods_brand,IFNULL(AVG(r.comment_rank), 0) AS comment_rank 
    from %s as g left join %s as c on g.cat_id=c.cat_id left join %s as b on 
     g.brand_id=b.brand_id left join %s as r on r.id_value=g.goods_id and r.comment_type
    = 0 and r.parent_id = 0 and r.status=1 where g.is_killer = 1 '''
    sql = sqlstr%(tables['goods'],tables['category'],tables['brand'],tables['comment'])
    rs=fetchone(sql)
    return rs
def search_goods(keywords,cat_id=0,size=10,page=1,order='sort_order',desc='desc'):
    '''
    Get search goods 
    '''
    if order in ['click_count', 'discount', 'salesvol', 'add_time', 'salesvol']:
        if desc==1:
            DB.order(order,'desc')
        else:
            DB.order(order)
    else:        
        DB.order('sort_order')
    

    select_fields = '''goods_id, goods_name,market_price, shop_price,
    attrs,discount,salesvol,promote_price, promote_start_date, promote_end_date,
     goods_brief, goods_thumb, goods_img,seller_id'''
    DB.select(select_fields)
    
    DB.where('cat_id',cat_id)
    DB.like('goods_name',keywords)
    DB.fm(tables['goods']).limit(size*(page-1),size)
    
    goods=DB.all()
    out = []
    return out

def search_num(keywords,cat_id=0):
    '''
    Get search goods number
    '''
    
    DB.select('count(*) as num')
    
    DB.where('cat_id',cat_id)
    DB.like('goods_name',keywords)
    DB.fm(tables['goods'])
    
    rs=DB.get()
    
    return rs['num']

def get_comment(goods_id, size = 10, page = 1):
    return get_data('comment',{'id_value':goods_id,'status':1},size,page)

def get_comment_num(goods_id, size = 10, page = 1):
    return get_count('comment',{'id_value':goods_id,'status':1})

