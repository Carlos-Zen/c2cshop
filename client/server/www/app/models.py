# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class CiSessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=45)
    user_agent = models.CharField(max_length=120)
    last_activity = models.IntegerField()
    user_data = models.TextField()
    class Meta:
        managed = False
        db_table = 'ci_sessions'

class CiSessionsCopy(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=45)
    user_agent = models.CharField(max_length=120)
    last_activity = models.IntegerField()
    user_data = models.TextField()
    class Meta:
        managed = False
        db_table = 'ci_sessions_copy'

class HrGoodsAttr(models.Model):
    goods_attr_id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    attr_id = models.IntegerField()
    attr_value = models.TextField()
    attr_price = models.CharField(max_length=255)
    attr_name = models.CharField(max_length=60, blank=True)
    attr_type = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField()
    is_pic = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hr_goods_attr'

class HrAccountLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    user_money = models.DecimalField(max_digits=10, decimal_places=2)
    frozen_money = models.DecimalField(max_digits=10, decimal_places=2)
    rank_points = models.IntegerField()
    pay_points = models.IntegerField()
    change_time = models.IntegerField()
    change_desc = models.CharField(max_length=255)
    change_type = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_account_log'

class HrAd(models.Model):
    ad_id = models.IntegerField(primary_key=True)
    position_id = models.IntegerField()
    media_type = models.IntegerField()
    ad_name = models.CharField(max_length=60)
    ad_link = models.CharField(max_length=255)
    ad_code = models.TextField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    link_man = models.CharField(max_length=60)
    link_email = models.CharField(max_length=60)
    link_phone = models.CharField(max_length=60)
    click_count = models.IntegerField()
    enabled = models.IntegerField()
    cat_id = models.IntegerField()
    sort_order = models.IntegerField()
    gcat_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ad'

class HrAdCat(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=60)
    parent_id = models.IntegerField()
    desc = models.CharField(max_length=150)
    sort_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ad_cat'

class HrAdCustom(models.Model):
    ad_id = models.IntegerField(primary_key=True)
    ad_type = models.IntegerField()
    ad_name = models.CharField(max_length=60, blank=True)
    add_time = models.IntegerField()
    content = models.TextField(blank=True)
    url = models.CharField(max_length=255, blank=True)
    ad_status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ad_custom'

class HrAdPosition(models.Model):
    position_id = models.IntegerField(primary_key=True)
    position_name = models.CharField(max_length=60)
    ad_width = models.IntegerField()
    ad_height = models.IntegerField()
    position_desc = models.CharField(max_length=255)
    position_style = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_ad_position'

class HrAdminAction(models.Model):
    action_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    action_code = models.CharField(max_length=20)
    relevance = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'hr_admin_action'

class HrAdminLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    log_time = models.IntegerField()
    user_id = models.IntegerField()
    log_info = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'hr_admin_log'

class HrAdminMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    sent_time = models.IntegerField()
    read_time = models.IntegerField()
    readed = models.IntegerField()
    deleted = models.IntegerField()
    title = models.CharField(max_length=150)
    message = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_admin_message'

class HrAdminUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=48)
    add_time = models.IntegerField()
    last_login = models.IntegerField()
    last_ip = models.CharField(max_length=15)
    action_list = models.TextField()
    nav_list = models.TextField()
    lang_type = models.CharField(max_length=50)
    agency_id = models.IntegerField()
    suppliers_id = models.IntegerField(blank=True, null=True)
    todolist = models.TextField(blank=True)
    role_id = models.IntegerField(blank=True, null=True)
    hr_salt = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'hr_admin_user'


class HrAffiliateLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    time = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=60, blank=True)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    point = models.IntegerField()
    separate_type = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_affiliate_log'

class HrAgency(models.Model):
    agency_id = models.IntegerField(primary_key=True)
    agency_name = models.CharField(max_length=255)
    agency_desc = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_agency'

class HrAreaRegion(models.Model):
    shipping_area_id = models.IntegerField(primary_key=True)
    region_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_area_region'

class HrArticle(models.Model):
    article_id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=30)
    author_email = models.CharField(max_length=60)
    keywords = models.CharField(max_length=255)
    article_type = models.IntegerField()
    is_open = models.IntegerField()
    add_time = models.IntegerField()
    file_url = models.CharField(max_length=255)
    open_type = models.IntegerField()
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'hr_article'

class HrArticleCat(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=255)
    cat_type = models.IntegerField()
    keywords = models.CharField(max_length=255)
    cat_desc = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    show_in_nav = models.IntegerField()
    parent_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_article_cat'

class HrAttrValue(models.Model):
    value_id = models.IntegerField(primary_key=True)
    attr_id = models.IntegerField()
    attr_value = models.CharField(max_length=150)
    sort_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_attr_value'

class HrAttribute(models.Model):
    attr_id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    attr_name = models.CharField(max_length=60)
    attr_input_type = models.IntegerField()
    attr_type = models.IntegerField()
    attr_values = models.TextField()
    attr_index = models.IntegerField()
    sort_order = models.IntegerField()
    is_linked = models.IntegerField()
    attr_group = models.IntegerField()
    is_pic = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_attribute'


class HrBackGoods(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    back_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField()
    product_id = models.IntegerField()
    product_sn = models.CharField(max_length=60, blank=True)
    goods_name = models.CharField(max_length=120, blank=True)
    brand_name = models.CharField(max_length=60, blank=True)
    goods_sn = models.CharField(max_length=60, blank=True)
    is_real = models.IntegerField(blank=True, null=True)
    send_number = models.IntegerField(blank=True, null=True)
    goods_attr = models.TextField(blank=True)
    goods_thumb = models.CharField(max_length=255)
    goods_number = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_back_goods'

class HrBackOrder(models.Model):
    back_id = models.IntegerField(primary_key=True)
    back_sn = models.CharField(max_length=20)
    order_sn = models.CharField(max_length=20)
    order_id = models.IntegerField()
    invoice_no = models.CharField(max_length=50, blank=True)
    add_time = models.IntegerField(blank=True, null=True)
    shipping_id = models.IntegerField(blank=True, null=True)
    shipping_name = models.CharField(max_length=120, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    action_user = models.CharField(max_length=30, blank=True)
    consignee = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=250, blank=True)
    country = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    sign_building = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=60, blank=True)
    zipcode = models.CharField(max_length=60, blank=True)
    tel = models.CharField(max_length=60, blank=True)
    mobile = models.CharField(max_length=60, blank=True)
    best_time = models.CharField(max_length=120, blank=True)
    postscript = models.CharField(max_length=255, blank=True)
    how_oos = models.CharField(max_length=120, blank=True)
    insure_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    suppliers_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    return_time = models.IntegerField(blank=True, null=True)
    agency_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    goods_thumb = models.CharField(max_length=255)
    goods_id = models.IntegerField()
    order_status = models.IntegerField()
    shipping_status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_back_order'


class HrBrand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=60)
    brand_logo = models.CharField(max_length=80)
    brand_desc = models.TextField()
    site_url = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    is_show = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_brand'

class HrBrandActivity(models.Model):
    special_id = models.IntegerField(primary_key=True)
    act_name = models.CharField(max_length=150)
    act_desc = models.CharField(max_length=255)
    act_type = models.IntegerField()
    brand_id = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    act_img = models.CharField(max_length=255)
    act_thumb = models.CharField(max_length=255)
    low_discount = models.FloatField()
    high_discount = models.FloatField()
    status = models.IntegerField()
    ext = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    is_promoted = models.IntegerField()
    brand_banner = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_brand_activity'

class HrCart(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    goods_id = models.IntegerField()
    goods_sn = models.CharField(max_length=60)
    product_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_number = models.IntegerField()
    goods_attr = models.TextField()
    is_real = models.IntegerField()
    extension_code = models.CharField(max_length=30)
    parent_id = models.IntegerField()
    rec_type = models.IntegerField()
    is_gift = models.IntegerField()
    is_shipping = models.IntegerField()
    can_handsel = models.IntegerField()
    goods_attr_id = models.CharField(max_length=255)
    goods_thumb = models.CharField(max_length=255)
    weight = models.IntegerField()
    act_type = models.IntegerField()
    price_degree = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_cart'

class HrCatRecommend(models.Model):
    cat_id = models.IntegerField()
    recommend_type = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_cat_recommend'

class HrCategory(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=90)
    keywords = models.CharField(max_length=255)
    cat_desc = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField()
    template_file = models.CharField(max_length=50)
    measure_unit = models.CharField(max_length=15)
    show_in_nav = models.IntegerField()
    style = models.CharField(max_length=150)
    is_show = models.IntegerField()
    grade = models.IntegerField()
    filter_attr = models.CharField(max_length=255)
    separator = models.IntegerField()
    is_promote = models.IntegerField()
    promote_name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_category'

class HrCollectGoods(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    goods_id = models.IntegerField()
    add_time = models.IntegerField()
    is_attention = models.IntegerField()
    cat_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_collect_goods'

class HrComment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    comment_type = models.IntegerField()
    id_value = models.IntegerField()
    email = models.CharField(max_length=60)
    user_name = models.CharField(max_length=60)
    content = models.TextField()
    comment_rank = models.IntegerField()
    add_time = models.IntegerField()
    ip_address = models.CharField(max_length=15)
    status = models.IntegerField()
    parent_id = models.IntegerField()
    user_id = models.IntegerField()
    rec_id = models.IntegerField()
    evaluate_rank = models.IntegerField()
    goods_rank = models.IntegerField()
    serve_rank = models.IntegerField()
    ship_rank = models.IntegerField()
    reply_content = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_comment'

class HrCrons(models.Model):
    cron_id = models.IntegerField(primary_key=True)
    cron_code = models.CharField(max_length=20)
    cron_name = models.CharField(max_length=120)
    cron_desc = models.TextField(blank=True)
    cron_order = models.IntegerField()
    cron_config = models.TextField()
    thistime = models.IntegerField()
    nextime = models.IntegerField()
    day = models.IntegerField()
    week = models.CharField(max_length=1)
    hour = models.CharField(max_length=2)
    minute = models.CharField(max_length=255)
    enable = models.IntegerField()
    run_once = models.IntegerField()
    allow_ip = models.CharField(max_length=100)
    alow_files = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_crons'

class HrDeliveryGoods(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    delivery_id = models.IntegerField()
    goods_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    product_sn = models.CharField(max_length=60, blank=True)
    goods_name = models.CharField(max_length=120, blank=True)
    brand_name = models.CharField(max_length=60, blank=True)
    goods_sn = models.CharField(max_length=60, blank=True)
    is_real = models.IntegerField(blank=True, null=True)
    extension_code = models.CharField(max_length=30, blank=True)
    parent_id = models.IntegerField(blank=True, null=True)
    send_number = models.IntegerField(blank=True, null=True)
    goods_attr = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'hr_delivery_goods'

class HrDeliveryOrder(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    delivery_sn = models.CharField(max_length=20)
    order_sn = models.CharField(max_length=20)
    order_id = models.IntegerField()
    invoice_no = models.CharField(max_length=50, blank=True)
    add_time = models.IntegerField(blank=True, null=True)
    shipping_id = models.IntegerField(blank=True, null=True)
    shipping_name = models.CharField(max_length=120, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    action_user = models.CharField(max_length=30, blank=True)
    consignee = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=250, blank=True)
    country = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    sign_building = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=60, blank=True)
    zipcode = models.CharField(max_length=60, blank=True)
    tel = models.CharField(max_length=60, blank=True)
    mobile = models.CharField(max_length=60, blank=True)
    best_time = models.CharField(max_length=120, blank=True)
    postscript = models.CharField(max_length=255, blank=True)
    how_oos = models.CharField(max_length=120, blank=True)
    insure_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    suppliers_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    agency_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hr_delivery_order'


class HrFavourableActivity(models.Model):
    act_id = models.IntegerField(primary_key=True)
    act_name = models.CharField(max_length=255)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    user_rank = models.CharField(max_length=255)
    act_range = models.IntegerField()
    act_range_ext = models.CharField(max_length=255)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    act_type = models.IntegerField()
    act_type_ext = models.DecimalField(max_digits=10, decimal_places=2)
    gift = models.TextField()
    sort_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_favourable_activity'

class HrFeedback(models.Model):
    msg_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=60)
    user_email = models.CharField(max_length=60)
    msg_title = models.CharField(max_length=200)
    msg_type = models.IntegerField()
    msg_status = models.IntegerField()
    msg_content = models.TextField()
    msg_time = models.IntegerField()
    message_img = models.CharField(max_length=255)
    order_id = models.IntegerField()
    msg_area = models.IntegerField()
    msg_types = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_feedback'

class HrFriendLink(models.Model):
    link_id = models.IntegerField(primary_key=True)
    link_name = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    link_logo = models.CharField(max_length=255)
    show_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_friend_link'

class HrGoods(models.Model):
    goods_id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    goods_sn = models.CharField(max_length=60)
    goods_name = models.CharField(max_length=120)
    goods_name_style = models.CharField(max_length=60)
    click_count = models.IntegerField()
    brand_id = models.IntegerField()
    provider_name = models.CharField(max_length=100)
    goods_number = models.IntegerField()
    goods_weight = models.DecimalField(max_digits=10, decimal_places=3)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2)
    promote_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_degree = models.CharField(max_length=100)
    promote_start_date = models.IntegerField()
    promote_end_date = models.IntegerField()
    warn_number = models.IntegerField()
    keywords = models.CharField(max_length=255)
    goods_brief = models.CharField(max_length=255)
    goods_desc = models.TextField()
    goods_thumb = models.CharField(max_length=255)
    goods_img = models.CharField(max_length=255)
    qr_img = models.CharField(max_length=255)
    is_real = models.IntegerField()
    extension_code = models.CharField(max_length=30)
    is_on_sale = models.IntegerField()
    is_alone_sale = models.IntegerField()
    is_shipping = models.IntegerField()
    integral = models.IntegerField()
    add_time = models.IntegerField()
    sort_order = models.IntegerField()
    is_delete = models.IntegerField()
    is_love = models.IntegerField()
    is_new = models.IntegerField()
    is_hot = models.IntegerField()
    is_promote = models.IntegerField()
    is_group = models.IntegerField()
    is_today = models.IntegerField()
    is_limit = models.IntegerField()
    bonus_type_id = models.IntegerField()
    last_update = models.IntegerField()
    goods_type = models.IntegerField()
    seller_note = models.CharField(max_length=255)
    give_integral = models.IntegerField()
    rank_integral = models.IntegerField()
    suppliers_id = models.IntegerField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    salesvol = models.IntegerField()
    is_killer = models.IntegerField()
    attrs = models.CharField(max_length=255)
    discount = models.FloatField()
    seller_id = models.IntegerField()
    shop_cat_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_goods'

class HrGoodsActivity(models.Model):
    act_id = models.IntegerField(primary_key=True)
    act_name = models.CharField(max_length=255)
    act_desc = models.TextField()
    act_type = models.IntegerField()
    goods_id = models.IntegerField()
    product_id = models.IntegerField()
    goods_name = models.CharField(max_length=255)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    is_finished = models.IntegerField()
    ext_info = models.TextField()
    is_promoted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_goods_activity'

class HrGoodsArticle(models.Model):
    goods_id = models.IntegerField()
    article_id = models.IntegerField()
    admin_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_goods_article'

class HrGoodsAttr(models.Model):
    goods_attr_id = models.IntegerField(primary_key=True)
    goods_id = models.ForeignKey(HrGoods)
    attr_id = models.IntegerField()
    attr_value = models.TextField()
    attr_price = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_goods_attr'


class HrGoodsGallery(models.Model):
    img_id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    img_url = models.CharField(max_length=255)
    img_desc = models.CharField(max_length=255)
    thumb_url = models.CharField(max_length=255)
    img_original = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_goods_gallery'

class HrGoodsType(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=60)
    enabled = models.IntegerField()
    attr_group = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_goods_type'


class HrKeywords(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.IntegerField()
    searchengine = models.CharField(max_length=20)
    keywords = models.CharField(max_length=90)
    count = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_keywords'


class HrMailTemplates(models.Model):
    template_id = models.IntegerField(primary_key=True)
    template_code = models.CharField(unique=True, max_length=30)
    is_html = models.IntegerField()
    template_subject = models.CharField(max_length=200)
    template_content = models.TextField()
    last_modify = models.IntegerField()
    last_send = models.IntegerField()
    type = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'hr_mail_templates'

class HrMemberPrice(models.Model):
    price_id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    user_rank = models.IntegerField()
    user_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'hr_member_price'

class HrNav(models.Model):
    id = models.IntegerField(primary_key=True)
    ctype = models.CharField(max_length=10, blank=True)
    cid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    ifshow = models.IntegerField()
    vieworder = models.IntegerField()
    opennew = models.IntegerField()
    url = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'hr_nav'

class HrOrderAction(models.Model):
    action_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    action_user = models.CharField(max_length=30)
    order_status = models.IntegerField()
    shipping_status = models.IntegerField()
    pay_status = models.IntegerField()
    action_place = models.IntegerField()
    action_note = models.CharField(max_length=255)
    log_time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_order_action'

class HrOrderGoods(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    goods_sn = models.CharField(max_length=60)
    product_id = models.IntegerField()
    goods_number = models.IntegerField()
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_attr = models.TextField()
    send_number = models.IntegerField()
    is_real = models.IntegerField()
    extension_code = models.CharField(max_length=30)
    parent_id = models.IntegerField()
    is_gift = models.IntegerField()
    goods_attr_id = models.CharField(max_length=255)
    goods_thumb = models.CharField(max_length=255)
    rec_type = models.IntegerField()
    is_back = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_order_goods'

class HrOrderInfo(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_sn = models.CharField(unique=True, max_length=20)
    user_id = models.IntegerField()
    order_status = models.IntegerField()
    shipping_status = models.IntegerField()
    pay_status = models.IntegerField()
    consignee = models.CharField(max_length=60)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=60)
    tel = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    best_time = models.CharField(max_length=120)
    sign_building = models.CharField(max_length=120)
    postscript = models.CharField(max_length=255)
    shipping_id = models.IntegerField()
    shipping_name = models.CharField(max_length=120)
    pay_id = models.IntegerField()
    pay_name = models.CharField(max_length=120)
    how_oos = models.CharField(max_length=120)
    how_surplus = models.CharField(max_length=120)
    pack_name = models.CharField(max_length=120)
    card_name = models.CharField(max_length=120)
    card_message = models.CharField(max_length=255)
    inv_payee = models.CharField(max_length=120)
    inv_content = models.CharField(max_length=120)
    goods_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    insure_fee = models.DecimalField(max_digits=10, decimal_places=2)
    pay_fee = models.DecimalField(max_digits=10, decimal_places=2)
    pack_fee = models.DecimalField(max_digits=10, decimal_places=2)
    card_fee = models.DecimalField(max_digits=10, decimal_places=2)
    money_paid = models.DecimalField(max_digits=10, decimal_places=2)
    surplus = models.DecimalField(max_digits=10, decimal_places=2)
    integral = models.IntegerField()
    integral_money = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    from_ad = models.IntegerField()
    referer = models.CharField(max_length=255)
    add_time = models.IntegerField()
    confirm_time = models.IntegerField()
    pay_time = models.IntegerField()
    shipping_time = models.IntegerField()
    pack_id = models.IntegerField()
    card_id = models.IntegerField()
    bonus_id = models.IntegerField()
    invoice_no = models.CharField(max_length=255)
    extension_code = models.CharField(max_length=30)
    extension_id = models.IntegerField()
    to_buyer = models.CharField(max_length=255)
    pay_note = models.CharField(max_length=255)
    agency_id = models.IntegerField()
    inv_type = models.CharField(max_length=60)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    is_separate = models.IntegerField()
    parent_id = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    is_deal = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_order_info'

class HrPack(models.Model):
    pack_id = models.IntegerField(primary_key=True)
    pack_name = models.CharField(max_length=120)
    pack_img = models.CharField(max_length=255)
    pack_fee = models.DecimalField(max_digits=6, decimal_places=2)
    free_money = models.IntegerField()
    pack_desc = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_pack'


class HrPayLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.IntegerField()
    is_paid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_pay_log'

class HrPayment(models.Model):
    pay_id = models.IntegerField(primary_key=True)
    pay_code = models.CharField(unique=True, max_length=20)
    pay_name = models.CharField(max_length=120)
    pay_fee = models.CharField(max_length=10)
    pay_desc = models.TextField()
    pay_order = models.IntegerField()
    pay_config = models.TextField()
    enabled = models.IntegerField()
    is_cod = models.IntegerField()
    is_online = models.IntegerField()
    pay_img = models.CharField(max_length=255)
    pay_type = models.IntegerField()
    pay_from = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_payment'

class HrPlugins(models.Model):
    code = models.CharField(primary_key=True, max_length=30)
    version = models.CharField(max_length=10)
    library = models.CharField(max_length=255)
    assign = models.IntegerField()
    install_date = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_plugins'

class HrProducts(models.Model):
    product_id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    goods_attr = models.CharField(max_length=50, blank=True)
    product_sn = models.CharField(max_length=60, blank=True)
    product_number = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hr_products'


class HrRegFields(models.Model):
    id = models.IntegerField(primary_key=True)
    reg_field_name = models.CharField(max_length=60)
    dis_order = models.IntegerField()
    display = models.IntegerField()
    type = models.IntegerField()
    is_need = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_reg_fields'

class HrRegion(models.Model):
    region_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    region_name = models.CharField(max_length=120)
    region_type = models.IntegerField()
    agency_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_region'

class HrRole(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=60)
    action_list = models.TextField()
    role_describe = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'hr_role'


class HrSessions(models.Model):
    sesskey = models.CharField(primary_key=True, max_length=32)
    expiry = models.IntegerField()
    userid = models.IntegerField()
    adminid = models.IntegerField()
    ip = models.CharField(max_length=15)
    user_name = models.CharField(max_length=60)
    user_rank = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    email = models.CharField(max_length=60)
    data = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_sessions'

class HrSessionsData(models.Model):
    sesskey = models.CharField(primary_key=True, max_length=32)
    expiry = models.IntegerField()
    data = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_sessions_data'

class HrShipping(models.Model):
    shipping_id = models.IntegerField(primary_key=True)
    shipping_code = models.CharField(max_length=20)
    shipping_name = models.CharField(max_length=120)
    shipping_desc = models.CharField(max_length=255)
    insure = models.CharField(max_length=10)
    support_cod = models.IntegerField()
    enabled = models.IntegerField()
    shipping_print = models.TextField()
    print_bg = models.CharField(max_length=255, blank=True)
    config_lable = models.TextField(blank=True)
    print_model = models.IntegerField(blank=True, null=True)
    shipping_price = models.DecimalField(max_digits=5, decimal_places=1)
    shipping_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_shipping'

class HrShippingArea(models.Model):
    shipping_area_id = models.IntegerField(primary_key=True)
    shipping_area_name = models.CharField(max_length=150)
    shipping_id = models.IntegerField()
    configure = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_shipping_area'

class HrShopConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    code = models.CharField(unique=True, max_length=30)
    type = models.CharField(max_length=10)
    store_range = models.CharField(max_length=255)
    store_dir = models.CharField(max_length=255)
    value = models.TextField()
    sort_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_shop_config'

class HrSms(models.Model):
    job_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    mobile = models.CharField(max_length=12)
    add_time = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_sms'

class HrSmsSend(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField()
    mobile = models.CharField(max_length=12)
    sms_content = models.TextField()
    error = models.IntegerField()
    last_send = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_sms_send'

class HrSnatchLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    snatch_id = models.IntegerField()
    user_id = models.IntegerField()
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_snatch_log'


class HrSuppliers(models.Model):
    suppliers_id = models.IntegerField(primary_key=True)
    suppliers_name = models.CharField(max_length=255, blank=True)
    suppliers_desc = models.TextField(blank=True)
    is_check = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_suppliers'

class HrTag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    goods_id = models.IntegerField()
    tag_words = models.CharField(max_length=255)
    is_hot = models.IntegerField()
    is_index = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_tag'



class HrUserAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    admin_user = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.IntegerField()
    paid_time = models.IntegerField()
    admin_note = models.CharField(max_length=255)
    user_note = models.CharField(max_length=255)
    process_type = models.IntegerField()
    payment = models.CharField(max_length=90)
    is_paid = models.IntegerField()
    user_name = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'hr_user_account'

class HrUserAddress(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address_name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    consignee = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    country = models.IntegerField()
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    address = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=60)
    tel = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    sign_building = models.CharField(max_length=120)
    best_time = models.CharField(max_length=120)
    is_default = models.IntegerField()
    add_time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_user_address'

class HrUserBonus(models.Model):
    bonus_id = models.IntegerField(primary_key=True)
    bonus_type_id = models.IntegerField()
    bonus_sn = models.BigIntegerField()
    user_id = models.IntegerField()
    used_time = models.IntegerField()
    order_id = models.IntegerField()
    emailed = models.IntegerField()
    bonus_content = models.TextField()
    class Meta:
        managed = False
        db_table = 'hr_user_bonus'

class HrUserFeed(models.Model):
    feed_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    value_id = models.IntegerField()
    goods_id = models.IntegerField()
    feed_type = models.IntegerField()
    is_feed = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_user_feed'

class HrUserProfiles(models.Model):
    user_id = models.IntegerField(primary_key=True)
    realname = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    company = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    chg_email = models.CharField(max_length=255, blank=True)
    addr = models.CharField(max_length=255, blank=True)
    countryid = models.IntegerField(blank=True, null=True)
    stateid = models.IntegerField(blank=True, null=True)
    cityid = models.IntegerField(blank=True, null=True)
    officfixline = models.CharField(max_length=32, blank=True)
    selfnote = models.TextField(blank=True)
    user_info = models.TextField(blank=True)
    user_icon = models.CharField(max_length=100, blank=True)
    reg_from = models.CharField(max_length=16, blank=True)
    reg_device = models.CharField(max_length=16, blank=True)
    district = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    ucode = models.CharField(max_length=32, blank=True)
    icon_file_to_s3 = models.IntegerField()
    alias = models.CharField(max_length=60, blank=True)
    class Meta:
        managed = False
        db_table = 'hr_user_profiles'

class HrUserRank(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_name = models.CharField(max_length=30)
    min_points = models.IntegerField()
    max_points = models.IntegerField()
    discount = models.FloatField()
    show_price = models.IntegerField()
    special_rank = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_user_rank'

class HrUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=60)
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=40)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    sex = models.IntegerField()
    birthday = models.DateField()
    user_money = models.DecimalField(max_digits=10, decimal_places=2)
    frozen_money = models.DecimalField(max_digits=10, decimal_places=2)
    pay_points = models.IntegerField()
    rank_points = models.IntegerField()
    addr = models.CharField(max_length=100, blank=True)
    reg_time = models.IntegerField()
    last_login = models.IntegerField()
    last_time = models.DateTimeField()
    last_ip = models.CharField(max_length=15)
    visit_count = models.IntegerField()
    user_rank = models.IntegerField()
    is_special = models.IntegerField()
    salt = models.CharField(max_length=10)
    parent_id = models.IntegerField()
    flag = models.IntegerField()
    alias = models.CharField(max_length=60)
    msn = models.CharField(max_length=60)
    qq = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    is_validated = models.IntegerField()
    credit_line = models.DecimalField(max_digits=10, decimal_places=2)
    passwd_question = models.CharField(max_length=50, blank=True)
    passwd_answer = models.CharField(max_length=255, blank=True)
    user_icon = models.CharField(max_length=255)
    active = models.IntegerField(blank=True, null=True)
    activation_key = models.CharField(max_length=32, blank=True)
    ucode = models.CharField(max_length=25, blank=True)
    realname = models.CharField(max_length=30, blank=True)
    province = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=20, blank=True)
    bind_email = models.IntegerField()
    bind_mobile = models.IntegerField()
    bind_email_key = models.CharField(max_length=32, blank=True)
    bind_email_str = models.CharField(max_length=60, blank=True)
    class Meta:
        managed = False
        db_table = 'hr_users'

class HrUshop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    service = models.IntegerField()
    desc_grade = models.IntegerField()
    atitude_grade = models.IntegerField()
    speed_grade = models.IntegerField()
    seller_id = models.IntegerField()
    logo = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    template_cat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ushop'

class HrUshopAd(models.Model):
    ad_id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    ad_name = models.CharField(max_length=60)
    ad_link = models.CharField(max_length=255)
    ad_code = models.TextField()
    click_count = models.IntegerField()
    enabled = models.IntegerField()
    sort_order = models.IntegerField()
    seller_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ushop_ad'

class HrUshopAdcat(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=60)
    parent_id = models.IntegerField()
    desc = models.CharField(max_length=150)
    sort_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ushop_adcat'

class HrUshopCat(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=90)
    keywords = models.CharField(max_length=255)
    cat_desc = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField()
    show_in_nav = models.IntegerField()
    is_show = models.IntegerField()
    seller_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ushop_cat'

class HrUshopNav(models.Model):
    nav_id = models.IntegerField(primary_key=True)
    nav_name = models.CharField(max_length=150)
    nav_url = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    seller_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_ushop_nav'

class HrUshopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    seller_name = models.CharField(max_length=255)
    real_name = models.CharField(max_length=255)
    seller_tel = models.CharField(max_length=15)
    seller_addr = models.CharField(max_length=255)
    seller_company = models.CharField(max_length=255)
    seller_email = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'hr_ushop_seller'

class HrVirtualCard(models.Model):
    card_id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    card_sn = models.CharField(max_length=60)
    card_password = models.CharField(max_length=60)
    add_date = models.IntegerField()
    end_date = models.IntegerField()
    is_saled = models.IntegerField()
    order_sn = models.CharField(max_length=20)
    crc32 = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_virtual_card'

class HrVote(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    vote_name = models.CharField(max_length=250)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    can_multi = models.IntegerField()
    vote_count = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_vote'

class HrVoteLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    vote_id = models.IntegerField()
    ip_address = models.CharField(max_length=15)
    vote_time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_vote_log'

class HrVoteOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    vote_id = models.IntegerField()
    option_name = models.CharField(max_length=250)
    option_count = models.IntegerField()
    option_order = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_vote_option'

class HrWholesale(models.Model):
    act_id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=255)
    rank_ids = models.CharField(max_length=255)
    prices = models.TextField()
    enabled = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_wholesale'

class HrOrderGoods(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_sn = models.CharField(max_length=20)
    order_status = models.IntegerField()
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.IntegerField()
    goods_name = models.CharField(max_length=120, blank=True)
    goods_thumb = models.CharField(max_length=255, blank=True)
    goods_id = models.IntegerField(blank=True, null=True)
    goods_number = models.IntegerField(blank=True, null=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_sn = models.CharField(max_length=60, blank=True)
    user_id = models.IntegerField()
    pay_status = models.IntegerField()
    shipping_status = models.IntegerField()
    is_back = models.IntegerField(blank=True, null=True)
    rec_id = models.IntegerField(blank=True, null=True)
    goods_attr = models.TextField(blank=True)
    pay_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'hr_order_goods'

class HrSaleOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_sn = models.CharField(max_length=20)
    order_status = models.IntegerField()
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.IntegerField()
    goods_name = models.CharField(max_length=120, blank=True)
    goods_thumb = models.CharField(max_length=255, blank=True)
    goods_id = models.IntegerField(blank=True, null=True)
    goods_number = models.IntegerField(blank=True, null=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_sn = models.CharField(max_length=60, blank=True)
    user_id = models.IntegerField()
    pay_status = models.IntegerField()
    shipping_status = models.IntegerField()
    is_back = models.IntegerField(blank=True, null=True)
    rec_id = models.IntegerField(blank=True, null=True)
    goods_attr = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'hr_sale_order'



