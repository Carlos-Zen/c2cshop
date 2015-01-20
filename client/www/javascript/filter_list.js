window.Product = Ember.Application.create();

Product.ApplicationAdapter = DS.FixtureAdapter.extend();

Product.Router.map(function () {
  this.resource('product', { path: '/' });
  
});
var page=1; //初始化显示页数
var size=5; //每页显示商品数目
$(function(){
	$(".m_lb_gd").click(function(){
	 page++;
	 pages = get_ws_data('cat_goods_num',{a:cat_id,b:brand_id,c:minprice,d:maxprice,e:attr1});; //cat_id, brand = 0, min = 0, max = 0, ext = '0.0.0.0'
	 var countpage=Math.ceil(pages/size)
	 if(countpage>=page){ 
	 var filter_goods = get_ws_data('prod_list',{a:cat_id,b:brand_id,c:minprice,d:maxprice,e:attr1,f:size,g:page,h:order,i:1});
	 var goods=productgoodss(filter_goods)
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
	str +='<div id="m_lb_pro" class="m_li_proc"><a href="activity.html?goods_id='+item.goods_id+'"><div class="m_lb_img"><img src='+item.goods_thumb+' width=100 height=100 ></div></a><div class="m_lb_prod"><div class="m_mszq_title"><a href="activity.html?goods_id='+item.goods_id+'">'+item.goods_name+'</a></div><div class="m_lb_yj"><span>￥'+item.shop_price+'</span><span id="m_lb_j">￥'+item.market_price+'</span></div><div class="m_lb_jg"><span>'+item.discount+'折</span><div class="m_lb_yj_m">'+item.salesvol+'人已购买</div></div></div></div>';
   }
	return str
}
function GetArgsFromHref(sHref, sArgName) 
{ 
var args = sHref.split("?");
 var retval = '';
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
 cat_id=GetArgsFromHref(sHref,sArgName)
var sArgName='order';
 order=GetArgsFromHref(sHref,sArgName)
var sArgName='brand_id';
 brand_id=GetArgsFromHref(sHref,sArgName)
var sArgName='min';
 minprice=GetArgsFromHref(sHref,sArgName)
var sArgName='max';
 maxprice=GetArgsFromHref(sHref,sArgName)
var sArgName='attr1';
 attr1=GetArgsFromHref(sHref,sArgName)
var sArgName='attr2';
 attr2=GetArgsFromHref(sHref,sArgName)
if(attr1==''){
	var attr1="0"
	}
if(attr2==''){
	var attr2="0"
	}


var attr=attr1+'.'+attr2

Product.ProductRoute = Ember.Route.extend({
  model: function () {

     filter = get_ws_data('prod_list',{a:cat_id,b:brand_id,c:minprice,d:maxprice,e:attr,f:size,g:page,h:order,i:1}); //筛选商品列表cat_id, brand = 0, min = 0, max = 0, ext = '0.0.0.0',size = 10, page = 1,order('click_count', 'shop_price', 'salesvol')
	 brand_filter = get_ws_data('cat_brands',{a:cat_id}); //过滤品牌字段
	 price_filter = get_ws_data('cat_interval',{a:cat_id,b:5}); //过滤价格字段
	 //alert(price_filter[2])
	 attr_filter = get_ws_data('cat_attr',{a:cat_id}); //过滤属性字段
	 console.log(filter);
	 var context ={};
	 context.filtergoods = filter;
	 context.brandfilter = brand_filter;
	// for(var i=0; i<price_filter.length; i++){
	 context.pricefilter1= price_filter[0];		
	 context.pricefilter2= price_filter[1];
	 context.pricefilter3= price_filter[2];
	 context.pricefilter4= price_filter[3];		
	 context.pricefilter5= price_filter[4];
	 context.pricefilter6= price_filter[5];
	// }
	 context.attrfilter = attr_filter;
	 
	 
	 context.catid={a:cat_id,b:brand_id,c:minprice,d:maxprice,e:attr1,h:order};
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
