// JavaScript Document
window.Ordersdetails = Ember.Application.create();

Ordersdetails.ApplicationAdapter = DS.FixtureAdapter.extend();

Ordersdetails.Router.map(function () {
  this.resource('ordersdetails', { path: '/' });
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
var sArgName='order_id';
var order_id=GetArgsFromHref(sHref,sArgName)
var sArgName='order_delete';
var order_delete=GetArgsFromHref(sHref,sArgName)
var sArgName='order_recover';
var order_recover=GetArgsFromHref(sHref,sArgName)
var sArgName='order_sn';         //订单号
var order_sn=GetArgsFromHref(sHref,sArgName)
var sArgName='order_name';       //订单名
var order_name=GetArgsFromHref(sHref,sArgName)
var sArgName='order_amount';     //订单金额
var order_amount=GetArgsFromHref(sHref,sArgName)
Ordersdetails.OrdersdetailsRoute = Ember.Route.extend({
  model: function () {
	 var user_content=ath.get_userinfo();
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 var user_val={'user_id':user_content.user_id,'is_login':login}
	 user_info = get_ws_data('get_user_info',{a:user_val}); //会员信息
	  if(order_sn!='' && order_name!='' && order_amount!=''){
	  order_pay = get_ws_data('get_pay',{a:'anxing2008@126.com',b:order_sn,c:order_name,d:order_amount}); //订单基本信息 a: 用户名 b: 订单编号  c:  订单名称  d:总价格
	  document.write(order_pay)
	  
	  }	  
	  
	  
	 /*if(order_delete != ''){
	 order_d = get_ws_data('delete_order',{a:18,b:order_delete}); //订单删除
	 order_id=order_delete
	  }*/
	  if(order_recover != ''){
	 order_d = get_ws_data('recover_order',{a:18,b:order_recover}); //订单订单恢复
	 order_id=order_recover
	  }
     order_infos = get_ws_data('order_info',{a:18,b:order_id}); //订单基本信息
	 order_goods_info = get_ws_data('order_goods',{a:18,b:order_id}); //订单商品基本信息
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); //会员信息
	 
		 if(order_infos.order_status==1){
			 order_infos.order_state="已完成";
			 }else if(order_infos.order_status==4){
			 order_infos.order_state="退货"; 
			 }else if(order_infos.order_status==2){	 
			 order_infos.order_state="已取消"; 
			 order_infos.order_recover="订单恢复"; 
			 order_infos.order_delete="订单删除";
			 }else if(order_infos.pay_status==0){
			 order_infos.order_cancel="订单取消";
			 order_infos.order_payment="立即支付";
			 order_infos.order_state="等待付款"; 	 
			 }else if((order_infos.pay_status==2) && (order_infos.shipping_status==4)){
			 order_infos.order_state=="等待提货";
			 }else if((order_infos.pay_status==2) && (order_infos.shipping_status==1)){
			 order_infos.order_state=="已发货"; 
			 }else if((order_infos.pay_status==2) && (order_infos.shipping_status==3)){
			 order_infos.order_state=="退货中"; 
			 }else if(order_infos.pay_status==2){
			 order_infos.order_state=="已付款"; 
			 }


	 console.log(order_infos);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.userinfo = user_info;
	 context.orderinfos = order_infos;
	 context.ordergoodsinfo = order_goods_info;
	 context.ordernum = order_num;
	 context.islogin = is_login;
	 return context;
  }
  
});


Ordersdetails.Ordersdetail = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





