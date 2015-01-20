from core.database.db_mysql import *
from common.phpserialize import *
from app.helper.common import cook_ext
from app.db import *
from common.phpserialize import *
from math import ceil

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
def get_category_goods(cat_id=0,brand = 0, min = 0, max = 0, ext\
     = '0.0.0.0', size = 10, page = 1, order, desc = 1):
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
    
    ext_list = cook_ext(ext)
    select_fields = '''goods_id, goods_name,market_price, shop_price,
    attrs,discount,salesvol,promote_price, promote_start_date, promote_end_date,
     goods_brief, goods_thumb, goods_img,seller_id'''
    DB.select(select_fields)
    

    DB.where('cat_id',cat_id)
    if brand>0:
        DB.where('brand_id',brand)
    if min>0:
        DB.where('shop_price',min,'>=')
    if max>0:
        DB.where('shop_price',max,'<=')
    
    DB.fm(tables['goods']).limit(size*(page-1),size)
    
    goods=DB.all()
    out = []
    for item in goods.keys():
        attrs=loads(goods[item].attrs)
        attr_diff=list(set(ext_list.values()).difference(set(attrs.values())))
        if not attr_diff:
            out.append(goods[item])
    return out

def get_category_goods_count(cat_id,brand = 0, min = 0, max = 0, ext= '0.0.0.0'):
    '''
    Get category goods count,used for goods category pages
    ''' 
    ext_list = cook_ext(ext)
    select_fields = '''goods_id, goods_name,market_price, shop_price,
    attrs,discount,salesvol,promote_price, promote_start_date, promote_end_date,
     goods_brief, goods_thumb, goods_img,seller_id'''
    DB.select(select_fields)
    
    if brand>0:
        DB.where('brand_id',brand)
    if min>0:
        DB.where('shop_price',min,'>=')
    if max>0:
        DB.where('shop_price',max,'<=')
    
    DB.fm(tables['goods'])
    
    goods=DB.all()
    out = []
    for item in goods.keys():
        attrs=loads(goods[item].attrs)
        attr_diff=list(set(ext_list.values()).difference(set(attrs.values())))
        if not attr_diff:
            out.append(goods[item])
    return len(out)
    
def get_promote_goods(cat_id=0,size=10,page=1,order='sort_order',desc=1):
    
    '''
    Get promote goods ,used for goods category pages
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
    goods=DB.all()
    return goods

def get_promote_num(cat_id=0,size=10,page=1):
    
    '''
    Get promote goods number,used for goods category pages
    '''
    select_fields = '''goods_id, goods_name,market_price, shop_price,
    attrs,discount,salesvol,promote_price, promote_start_date, promote_end_date,
     goods_brief, goods_thumb, goods_img,seller_id'''
    DB.select(select_fields)
    DB.where('cat_id',cat_id)
    goods=DB.all()
    return goods

def get_cat_attr(cat_id):
    DB.select('filter_attr').fm(tables['category']).where('cat_id',cat_id)
    rs=DB.get()
    filter = rs['filter_attr']
    DB.select('attr_id,attr_name').fm(tables['attribute']).where('attr_type',0).where_in('attr_id',filter)
    attrs = DB.all()
    for i in range(len(attrs)):
        DB.select('value_id,attr_value').fm(tables['attr_value']).where('attr_id',attrs[i]['attr_id'])
        attrs[i]['attrs']=DB.all()
    return attrs

def cat_price_interval(cat_id,separator):
    DB.select("MIN(shop_price) as minp,MAX(shop_price) as maxp").fm(tables['goods']).where('cat_id',cat_id)
    row=DB.get()
    interval = ceil((row['maxp']-row['minp'])/separator)
    startp = row['minp']
    endp = row['maxp']
    prices = [startp+(i*interval) for i in range(separator)]
    return prices

def get_categories_tree(cat_id=0):
    '''
    get category sons and brothers tree like by cat_id
    '''
    if cat_id>0:
        rs = DB.select('parent_id').fm(tables['category']).where('cat_id',cat_id).get()
        parent_id = rs['parent_id']
    else:
        parent_id = 0
    rs=DB.select('count(*)').fm(tables['category']).where({'parent_id':parent_id,'is_show':1}).get()
    out = []
    if rs or parent_id==0:
        rs=DB.select('cat_id,cat_name ,parent_id,is_show').fm(tables['category'])\
        .where({'parent_id':parent_id,'is_show':1}).order('sort_order','ASC').all()
        for item in rs:
            temp={}
            if item['is_show']:
                temp['id']=item['id']
                temp['cat_name']=item['cat_name']
                temp['sons'] = get_child_tree(item['cat_id'])
                out.append(temp)
    return out

def get_child_tree(cat_id=0):
    '''
    get category sons tree like by cat_id
    '''
    rs=DB.select('count(*)').fm(tables['category']).where({'parent_id':cat_id,'is_show':1}).get()
    out = []
    if rs or cat_id==0:
        rs=DB.select('cat_id,cat_name ,parent_id,is_show').fm(tables['category'])\
        .where({'parent_id':cat_id,'is_show':1}).order('sort_order','ASC').all()
        for item in rs:
            temp={}
            if item['is_show']:
                temp['id']=item['id']
                temp['cat_name']=item['cat_name']
                temp['sons'] = get_child_tree(item['cat_id'])
                out.append(temp)
    return out
                


        
