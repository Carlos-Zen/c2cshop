window.Product = Ember.Application.create();

Product.ApplicationAdapter = DS.FixtureAdapter.extend();

Product.Router.map(function () {
  this.resource('product', { path: '/' });
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
var sArgName='cat_id';
var cat_id=GetArgsFromHref(sHref,sArgName)
Product.ProductRoute = Ember.Route.extend({
  model: function () {
	  
	 var catlist = localStorage.getItem("catlist");
	 var thirdcatlist = localStorage.getItem("thirdcatlist"); 
	 if(catlist!=null){
	 	 catlist = JSON.parse(catlist);
		 thirdcatlist = JSON.parse(thirdcatlist);
	 }else{
		 catlist = get_ws_data('prod_cat',{a:0}); //分类列表 一级 和  二级   //侧滑栏分类
		 thirdcatlist = get_ws_data('child_cat',{a:cat_id}); //分类列表 三级
		 localStorage.setItem("catlist",JSON.stringify(catlist));
		 localStorage.setItem("thirdcatlist",JSON.stringify(thirdcatlist));
	 }	
	 //cat = get_ws_data('prod_cat',{a:0}); 

	 console.log(thirdcatlist);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};

	 context.catlistgoods = catlist;
	 context.thirdcat = thirdcatlist;
	 context.catgoods = catlist;  //cat
	 context.islogin = is_login;
	  if(is_login){
		var user_content=ath.get_userinfo()
		context.loginname = user_content.user_name;
	  }
	 return context;
  }
});

Product.Goods = DS.Model.extend({
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
