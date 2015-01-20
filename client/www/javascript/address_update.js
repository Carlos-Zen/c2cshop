// JavaScript Document
window.Updateaddress = Ember.Application.create();

Updateaddress.ApplicationAdapter = DS.FixtureAdapter.extend();

Updateaddress.Router.map(function () {
  this.resource('updateaddress', { path: '/' });
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
var sArgName='address_id';
var address_id=GetArgsFromHref(sHref,sArgName)
Updateaddress.UpdateaddressRoute = Ember.Route.extend({
  model: function () {
	 var user_content=ath.get_userinfo();
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 var user_val={'user_id':user_content.user_id,'is_login':login}
	 user_info = get_ws_data('get_user_info',{a:user_val}); //会员信息
	 address_update = get_ws_data('address_info',{a:address_id}); //修改收货地址展示
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); //会员信

	 console.log(address_update);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.userinfo = user_info;
	 context.addressupdate = address_update;
	 context.ordernum = order_num;
	 context.addressid = address_id;
	 context.islogin = is_login;
	 return context;
  }
  
});


Updateaddress.Updateaddres = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





