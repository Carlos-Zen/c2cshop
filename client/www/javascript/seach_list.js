window.Product = Ember.Application.create();

Product.ApplicationAdapter = DS.FixtureAdapter.extend();

Product.Router.map(function () {
  this.resource('product', { path: '/' });
});

setTimeout( function(){  //自动获取文本框焦点
  try{
    document.getElementById('m_lb_seac').focus();
  } catch(e){}
}, 200);
var page=1; //初始化显示页数
var size=10; //每页显示商品数目
$(function(){
	$(".m_lb_gd").click(function(){
	 page++;
	 pages = get_ws_data('search_num',{a:0,b:0,c:0,d:0});; //商品购买数量$keywords, $cat = 0, $min = 0, $max = 0
	 var countpage=Math.ceil(pages/size)
	 if(countpage>=page){ 
	 var seach_goods = get_ws_data('search',{a:searchs,b:0,c:size,d:page,e:order,f:0,g:0,h:1});
	 var goods=productgoodss(seach_goods)
	 $("#appending").append(goods)
	 }
	 if(countpage==page){ 
	 $(".m_lb_gd").remove();
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
	str +='<div id="m_lb_pro" class="m_li_proc"><a href="activity.html?goods_id='+item.goods_id+'"><div class="m_lb_img"><img src='+item.goods_thumb+' width=100 height=100 ></div></a><div class="m_lb_prod"><div class="m_mszq_title"><a href="activity.html?goods_id='+item.goods_id+'">'+item.goods_name+'</a></div><div style="display:none" class="p_time"> <span>'+item.promote_start_date+' '+item.promote_end_date+'</span> </div><div class="m_lb_yj"><span>￥'+item.promote_price+'</span><span id="m_lb_j">￥'+item.shop_price+'</span></div><div class="m_lb_jg"><span>'+item.discount+'折</span><div class="m_lb_yj_m">'+item.salesvol+'人已购买</div></div></div></div>';
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
var sArgName='order';
var order=GetArgsFromHref(sHref,sArgName)
var sArgName='searchs';
 searchs=decodeURI(GetArgsFromHref(sHref,sArgName))
Product.ProductRoute = Ember.Route.extend({
  model: function () {

     seach = get_ws_data('search',{a:searchs,b:0,c:size,d:page,e:order,f:0,g:0,h:1}); //商品搜索列表 $keywords, $cat_id = 0, $size=10, $page=1, $order, $min, $max , $desc
	 cat = get_ws_data('prod_cat',{a:0}); //侧滑栏分类
	 //comments_promise = get_ws_data('promote_goods',{a:0,b:2});
	 console.log(seach);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.seachgoods = seach;
	 context.catgoods = cat;
	 //context.comments = comments_promise;
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
