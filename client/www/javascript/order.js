// JavaScript Document
window.Orders = Ember.Application.create();

Orders.ApplicationAdapter = DS.FixtureAdapter.extend();

Orders.Router.map(function () {
  this.resource('orders', { path: '/' });
});

function GetArgsFromHref(sHref, sArgName) 
{ 
var args = sHref.split("?");
 var retval = "";
 if(args[0] == sHref) /*参数为空*/
 { 
return retval; /*无需做任何处理*/ 
}
 var str = args[1];
 args = str.split("&"); 
for(var i = 0; i < args.length; i ++)
 { 
str = args[i]; 
var arg = str.split("=");
 if(arg.length <= 1) continue; 
if(arg[0] == sArgName) 
retval = arg[1];
 }
 return retval;
 }
var sHref=window.location.href;
var sArgName='count_price';
var count_price=GetArgsFromHref(sHref,sArgName)
Orders.OrdersRoute = Ember.Route.extend({
  model: function () {
	 var user_content=ath.get_userinfo();
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 var user_val={'user_id':user_content.user_id,'is_login':login}
	 user_info = get_ws_data('get_user_info',{a:user_val}); //会员信息
	 address_list = get_ws_data('address_list',{a:user_content.user_id,b:1}); //收货地址
	 payment_list = get_ws_data('payment_list',{a:0,b:1}); //选择支付方式
     shipping_list = get_ws_data('shipping_list',{a:0}); //物流配送方式
	 address_update = get_ws_data('address_info',{a:address_list[0].address_id}); //修改收货地址显示

	 console.log(user_content.user_id);
	 
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.userinfo = user_info;
	 context.addresslist = address_list;
	 context.paymentlist = payment_list;
	 context.shippinglist = shipping_list;
	 context.countprice = count_price;  //商品总价格，不包括邮费
	 context.addressupdate = address_update;
	 context.islogin = is_login;
	 
	
	 return context;
  }
  
});


Orders.Order = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





