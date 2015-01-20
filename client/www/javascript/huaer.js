window.Huaer = Ember.Application.create();

Huaer.ApplicationAdapter = DS.FixtureAdapter.extend();

Huaer.Router.map(function () {
  this.resource('huaer', { path: '/' });
});

Huaer.HuaerRoute = Ember.Route.extend({
  model: function () {
	 brandadvert = get_ws_data('cat_ad',{a:49});  //首页轮播广告
     spilke = get_ws_data('get_sec_desc',{a:0});  //秒杀
	 group = get_ws_data('group_list',{a:0,b:0,c:0,d:0,e:'0.0.0.0',f:4,g:1,h:'salesvol',i:1}); //团购专区 cat_id, brand = 0, min = 0, max = 0, ext = '0.0.0.0',siz e  = 10, page = 1,order('click_count', 'shop_price', 'salesvol')
	 advert = get_ws_data('get_ad',{a:316});  //活动区广告
	 activity = get_ws_data('recommend_goods',{b:'hot',c:0,d:2});  //活动专区商品 type $cat_id, $size 
	 brand = get_ws_data('special_actlist',{a:0,b:3,c:1,d:'on'}); //品牌专区$cat_id = 0, $size = 10, $page = 1, $condition = 'on' 
	 cat = get_ws_data('prod_cat',{a:0}); //侧滑栏分类
	 console.log(brandadvert);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.brandadvertgoods = brandadvert;
	 context.goods = spilke;
	 context.groupgoods = group;
	 context.advertgoods = advert;
	 context.activitygoods = activity;
	 context.brandgoods = brand;
	 context.catgoods = cat;
	 return context;
  }
});


/*function group_model(){
	data=get_ws_data('group_list',{a:0,b:0,c:0,d:0,e:'0.0.0.0',f:5,g:1,h:'salesvol',i:1});
	data.goods_name= 
	return data
	}*/



Huaer.Group = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  discount: DS.attr('string'),
  start_time: DS.attr('string'),
  end_time: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});

