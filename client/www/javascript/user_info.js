// JavaScript Document
window.Userinfo = Ember.Application.create();

Userinfo.ApplicationAdapter = DS.FixtureAdapter.extend();

Userinfo.Router.map(function () {
  this.resource('userinfo', { path: '/' });
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
var sArgName='login_out';
var login_out=GetArgsFromHref(sHref,sArgName)
var sArgName='from';
var from=GetArgsFromHref(sHref,sArgName)
Userinfo.UserinfoRoute = Ember.Route.extend({
  model: function () {
	  

	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 if(is_login){
		var user_content=ath.get_userinfo();
		var user_val={'user_id':user_content.user_id,'is_login':login}
		user_info = get_ws_data('get_user_info',{a:user_val}); //会员信息	 
	 }
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); //会员信息	 
	 if(login_out=='ok'){
		ath.out_login();	 
	 }
	 console.log(user_info);
	 
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 if(is_login){
	 context.userinfo = user_info;
	 }
	 context.ordernum = order_num;
	 context.islogin = is_login;
	 context.fromlogin = from;

	 return context;
  }
  
});





