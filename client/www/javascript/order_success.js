// JavaScript Document
window.Ordersuccesss = Ember.Application.create();

Ordersuccesss.ApplicationAdapter = DS.FixtureAdapter.extend();

Ordersuccesss.Router.map(function () {
  this.resource('ordersuccesss', { path: '/' });
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
var sArgName='order';
var order=GetArgsFromHref(sHref,sArgName)
var sArgName='count_price';
var count_price=GetArgsFromHref(sHref,sArgName)
var sArgName='address_id';
var address_id=GetArgsFromHref(sHref,sArgName)
var sArgName='shipping_id';
var shipping_id=GetArgsFromHref(sHref,sArgName)
var sArgName='payment_id';
var payment_id=GetArgsFromHref(sHref,sArgName)
var sArgName='invoice_type';
var invoice_type=unescape(GetArgsFromHref(sHref,sArgName))
var sArgName='invoice_commercial';
var invoice_commercial=unescape(GetArgsFromHref(sHref,sArgName))
var sArgName='invoice_info';
var invoice_info=unescape(GetArgsFromHref(sHref,sArgName))
var sArgName='order_remark_info';
var order_remark_info=unescape(GetArgsFromHref(sHref,sArgName))
Ordersuccesss.OrdersuccesssRoute = Ember.Route.extend({
  model: function () {
	 var user_content=ath.get_userinfo()
	 var inv_note={'inv_payee':invoice_commercial,'inv_type':invoice_type,'inv_content':invoice_info,'pay_note':order_remark_info}
	 order_ok = get_ws_data('cr_order',{a:user_content.user_id,b:address_id,c:shipping_id,d:payment_id,e:inv_note}); //生成订单
	 order_paying = get_ws_data('get_pay',{a:'anxing2008@126.com',b:order_ok.order_sn,c:order_ok.order_sn,d:order_ok.order_amount}); //订单基本信息 a: 用户名 b: 订单编号  c:  订单名称  d:总价格
	 if(order=='ok'){
	 document.write(order_paying);
	 }
	 console.log(order_ok);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};

	 context.order_ok = order_ok;
	 context.islogin = is_login;
	 context.loginname = user_content.user_name;
	 return context;
	 
  }
  
});

Ordersuccesss.Ordersuccess = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





