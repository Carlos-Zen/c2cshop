// JavaScript Document
window.Todos = Ember.Application.create();

Todos.ApplicationAdapter = DS.FixtureAdapter.extend();

Todos.Router.map(function () {
  this.resource('todos', { path: '/' });
});

Todos.TodosRoute = Ember.Route.extend({
  model: function () {

     spike_info = get_ws_data('get_sec_info',{a:0}); //商品基本
	 spike_attr = get_ws_data('goods_attr',{a:spike_info.goods_id}); //商品基本规格属性
	 //goods_imgs = get_ws_data('goods_imgs',{a:118}); //商品图片
	 spike_buy_attr = get_ws_data('goods_buy_attr',{a:spike_info.goods_id}); //商品购买属性
	 spike_comments = get_ws_data('get_comment',{a:spike_info.goods_id,b:5,c:1}); //商品评论 goods_id,size,page
	 cat = get_ws_data('prod_cat',{a:0}); //侧滑栏分类
	 console.log(spike_info);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.spikegoods = spike_info;
	 context.spikeattr = spike_attr;
	 //context.goodsimgs = goods_imgs;
	 context.spikebuyattr = spike_buy_attr;
	 context.spikecomments = spike_comments;
	 context.catgoods = cat;
	 context.islogin = is_login;
	  if(is_login){
		var user_content=ath.get_userinfo()
		context.loginname = user_content.user_name;
	  }	
	 return context;
  }
  
});


Todos.Todo = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





