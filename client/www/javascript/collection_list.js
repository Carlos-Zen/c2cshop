// JavaScript Document
window.Collections = Ember.Application.create();

Collections.ApplicationAdapter = DS.FixtureAdapter.extend();

Collections.Router.map(function () {
  this.resource('collections', { path: '/' });
});
var user_content=ath.get_userinfo();
var page=1; //初始化显示页数
var size=10; //每页显示商品数目
$(function(){
	$(".con_duo").click(function(){
	 page++;
	 pages = get_ws_data('collect_num',{a:user_content.user_id,c:0});; //商品订单数量 
	 var countpage=Math.ceil(pages/size)
	 if(countpage>=page){ 
	 var collect_list = get_ws_data('collect_list',{a:user_content.user_id,c:0,d:size,e:page}); //订单列表
	 
	 console.log(collect_list);
	 var collect=productgoodss(collect_list)
	 $("#appending").append(collect)
	 }
	 if(countpage==page){ 
	 $(".con_duo").remove();
	 }
	})
	
})
function productgoodss(group){
	for(var i=0;i<group.length;i++){
	item = group[i];
	var str;
	if(typeof(str)=='undefined'){
		str='';
		}	
	str +='<div class="store_chan"> <div class="store_left"> <img src='+item.goods_thumb+' width=100 height=100 /> </div> <div class="store_right"> <p class="store_title">'+item.goods_name+'</p> <p><span class="store_sale">商城价</span><span class="con_color">￥</span> <span class="store_price">'+item.shop_price+'</span> <span class="store_biao"></span> </p> <p>原价：<span class="price_y">￥'+item.market_price+'</span></p> <!--<p>结束日期：2013-12-25</p>--> <p><span class="store_cart"onclick="add_cart('+item.goods_id+')">放入购物车</span><span class="store_buy"><a href="collection_list.html?rec_id='+item.rec_id+'">删除</a></span> </p> </div>  </div>';
   }
	return str
}
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
var sArgName='rec_id';
var rec_id=GetArgsFromHref(sHref,sArgName)
Collections.CollectionsRoute = Ember.Route.extend({
  model: function () {
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 var user_val={'user_id':user_content.user_id,'is_login':login}
	 user_info = get_ws_data('get_user_info',{a:user_val}); //会员信息
	  if(rec_id != ''){
	 order_d = get_ws_data('cancel_collect',{a:user_content.user_id,b:rec_id}); //收藏商品删除
	  }
	 collection_list = get_ws_data('collect_list',{a:user_content.user_id,c:0,d:size,e:page}); //收藏商品列表
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); //会员信
	 console.log(collection_list);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.userinfo = user_info;
	 context.collectionlist = collection_list;
	 context.ordernum = order_num;
	 context.islogin = is_login;
	 
	
	 return context;
  }
  
});


Collections.collections = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





