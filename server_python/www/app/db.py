from core.database.db_mysql import *
from common.setting import *

tables = {}
tables['goods'] = ''.join([db_pre,'goods'])
tables['attr_value'] = ''.join([db_pre,'attr_value'])
tables['attribute'] = ''.join([db_pre,'attribute'])
tables['goods_attr'] = 'goods_attr'
tables['attrs'] = db_pre,'goods'
tables['brand'] = ''.join([db_pre,'brand'])
tables['comment'] = ''.join([db_pre,'comment'])
tables['category'] = ''.join([db_pre,'category'])
tables['goods_gallery'] = ''.join([db_pre,'goods_gallery'])
tables['brand_activity'] = ''.join([db_pre,'brand_activity'])
tables['goods_activity'] = ''.join([db_pre,'goods_activity'])
tables['brand'] = ''.join([db_pre,'brand'])
tables['ad'] = ''.join([db_pre,'ad'])
tables['adcat'] = ''.join([db_pre,'ad_cat'])
tables['comment'] = ''.join([db_pre,'comment'])
tables['shipping'] = ''.join([db_pre,'shipping'])
tables['address'] = ''.join([db_pre,'user_address'])
tables['payment'] = ''.join([db_pre,'payment'])
tables['collect'] = ''.join([db_pre,'collect_goods'])
DB=Db_mysql()