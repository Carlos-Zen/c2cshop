// JavaScript Document
window.Todos = Ember.Application.create();

Todos.ApplicationAdapter = DS.FixtureAdapter.extend();

Todos.Router.map(function () {
  this.resource('todos', { path: '/' });
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
var sArgName='goods_id';
var id=GetArgsFromHref(sHref,sArgName)
Todos.TodosRoute = Ember.Route.extend({
  model: function () {
	 var goods_info = localStorage.getItem("goods_info");
	 var comments_promise = localStorage.getItem("comments_promise");
	 var goods_buy_attr = localStorage.getItem("goods_buy_attr");
	 
	 var cat = localStorage.getItem("cat");
	 if(cat!=null){
	 	 cat = JSON.parse(cat);
	 }else{
		 cat = get_ws_data('prod_cat',{a:0}); //侧滑栏分类
		 localStorage.setItem("cat",JSON.stringify(cat));
	 }	 
	 
	 if(goods_info!=null){
		 goods_info = JSON.parse(goods_info);
		 comments_promise = JSON.parse(comments_promise);
		 goods_buy_attr = JSON.parse(goods_buy_attr);
		 }else{
		 goods_info = get_ws_data('goods_all',{a:id}); //商品基本
		 //goods_imgs = get_ws_data('goods_imgs',{a:118}); //商品图片
		 comments_promise = get_ws_data('get_comment',{a:id,b:5,c:1}); //商品评论 goods_id,size,page
		 goods_buy_attr = get_ws_data('goods_buy_attr',{a:id}); //商品购买属性

		
	 }

	 
	 
	 console.log(goods_info);
	 var context ={};
	 context.goodsinfo = goods_info;
	 //context.goodsimgs = goods_imgs;
	 context.comments = comments_promise;
	 context.goodsbuyattr = goods_buy_attr;
	 context.catgoods = cat;
	 context.islogin = is_login;
	  if(is_login){
		var user_content=ath.get_userinfo()
		context.loginname = user_content.user_name;
	  }
	
//	  var get_data = function(){
	 	return context;
//	  }
/*	  return new Ember.RSVP.Promise(function(resolve) {
	    Ember.run.later(function() {
		resolve(get_data());
	    }, 50);
	  });*/
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





