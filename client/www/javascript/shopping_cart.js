// JavaScript Document
window.Cart = Ember.Application.create();

Cart.ApplicationAdapter = DS.FixtureAdapter.extend();

Cart.Router.map(function () {
  this.resource('cart', { path: '/' });
});

if(is_login){ //此处判断是否登录
	shopping_cart=new cart();
	var user_content=ath.get_userinfo();
	 goods_all=shopping_cart.addgetall()
	 for(var i=0; i<goods_all.length; i++){
		item = goods_all[i];
		var goods= {'user_id':user_content.user_id,'goods_id':item.goods_id,'goods_number':item.goods_number}
		insert_goods = get_ws_data('cart_insert',{a:goods}); //登陆后本地购物车产品加入购物车库
		 }
	shopping_cart.clear();
	}


shopping_cart=new cart();
var cart_goods=shopping_cart.getall()

Cart.CartRoute = Ember.Route.extend({
  model: function () { 
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	if(is_login){
	 var user_content=ath.get_userinfo();
	 var user_val={'user_id':user_content.user_id,'is_login':login}
	 user_info = get_ws_data('get_user_info',{a:user_val}); //获取用户信息
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); 
	 uder_id=user_content.user_id;
	}
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.cartgoods = cart_goods;
	if(is_login){
	 context.userinfo = user_info;
	 context.ordernum = order_num;
	}

	 context.islogin = is_login;
	 return context;
  }
  
});


Cart.cartgoods = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





