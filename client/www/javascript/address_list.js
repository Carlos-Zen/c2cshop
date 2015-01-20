// JavaScript Document
window.Addresslists = Ember.Application.create();

Addresslists.ApplicationAdapter = DS.FixtureAdapter.extend();

Addresslists.Router.map(function () {
  this.resource('addresslists', { path: '/' });
});
var user_content=ath.get_userinfo();
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
var sArgName='address_id';
var address_id=GetArgsFromHref(sHref,sArgName)
Addresslists.AddresslistsRoute = Ember.Route.extend({
  model: function () {
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 if(address_id != ''){
	 delete_address = get_ws_data('delete_address',{a:user_content.user_id,d:address_id}); //订单地址删除
	 }
	 var user_val={'user_id':user_content.user_id,'is_login':login}
     user_info = get_ws_data('get_user_info',{a:user_val}); //会员基本信息
	 address_list = get_ws_data('address_list',{a:user_content.user_id,d:5}); //订单列表
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); //会员信息
	 console.log(login);
	 console.log(user_content.user_id);
	 console.log(user_info);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.userinfo = user_info;
	 context.addresslist = address_list;
	 context.ordernum = order_num;
	 context.islogin = is_login;
	 
	
	 return context;
  }
  
});


Addresslists.Addresslist = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





