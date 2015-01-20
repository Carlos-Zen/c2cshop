window.Product = Ember.Application.create();

Product.ApplicationAdapter = DS.FixtureAdapter.extend();

Product.Router.map(function () {
  this.resource('product', { path: '/' });
});
var page=1; //初始化显示页数
var size=10; //每页显示商品数目
/*test = function(){
		$("#ssss").click(function(){
					alert($(this).html());
			})};
Ember.run.later(function() {
      test();
      }, 2000);*/

$(function(){
	$(".m_lb_gd").click(function(){
	 page++;
	 pages = get_ws_data('special_actnum',{a:0});; //商品购买数量 cat_id
	 var countpage=Math.ceil(pages/size)
	 if(countpage>=page){ 
	 var activity_goods = get_ws_data('special_actlist',{a:0,b:size,c:page,d:'on'});
	 var goods=productgoodss(activity_goods)
	 $("#appending").append(goods)
	 }
	 btime()
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
	str +='<div class="mob_skill"><div class="act_time"><span class="tu"></span ><span class="brandtime"></span></div><div class="b_time" style="display:none"> <span>'+item.start_time+'</span><span>'+item.end_time+'</span></div><div class="mob_skill_img"><a href="./sale_list.html?brand_id='+item.brand_id+'"><img src='+item.act_img+' width=304 height=132 border="0"></a></div><div class="mob_skill_title"><span style=" font-size:13px; font-weight:bold;"><a href="./sale_list.html?brand_id='+item.brand_id+'">'+item.act_name+'</a></span><span class="act_right"> <span class="act_r">'+item.low_discount+'-'+item.high_discount+'折</span> </span>	</div></div>';
   }
	return str
}
Product.ProductRoute = Ember.Route.extend({
  model: function () {
	 var brand_list = localStorage.getItem("brand_list");
	 var cat = localStorage.getItem("cat");
	 if(cat!=null){
	 	 cat = JSON.parse(cat);
	 }else{
		 cat = get_ws_data('prod_cat',{a:0}); //侧滑栏分类
		 localStorage.setItem("cat",JSON.stringify(cat));
	 }	 
	  
	 if(brand_list!=null){
	 	 brand_list = JSON.parse(brand_list);
	 }else{
     	 brand_list = get_ws_data('special_actlist',{a:0,b:size,c:page,d:'on'}); //品牌商品列表 $cat_id = 0, $size = 10, $page = 1, $condition = 'on' 
		 localStorage.setItem("brand_list",JSON.stringify(brand_list));
	 }	   

	 console.log(brand_list);
	 var context ={};
	 context.brandlistgoods = brand_list;
	 context.catgoods = cat;
	 context.islogin = is_login;
	  if(is_login){
		var user_content=ath.get_userinfo()
		context.loginname = user_content.user_name;
	  }
//	  var get_data = function(){
	 	return context;
//	  } 
/*	return new Ember.RSVP.Promise(function(resolve) {
      Ember.run.later(function() {
        resolve(get_data());
      }, 50);
    });*/
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
