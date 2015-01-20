// JavaScript Document
window.Orderlists = Ember.Application.create();

Orderlists.ApplicationAdapter = DS.FixtureAdapter.extend();

Orderlists.Router.map(function () {
  this.resource('orderlists', { path: '/' });
});
var user_content=ath.get_userinfo();
var page=1; //初始化显示页数
var size=10; //每页显示商品数目
$(function(){
	$(".con_duo").click(function(){
	 page++;
	 pages = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0});; //商品订单数量 
	 var countpage=Math.ceil(pages/size)
	 if(countpage>=page){ 
	 var order_list = get_ws_data('order_list',{a:user_content.user_id,b:'',c:0,d:size,e:page}); //订单列表
	 
	 console.log(order_list);
	 var orders=productgoodss(order_list)
	 $("#appending").append(orders)
	 }
	 addtime();
	 if(countpage==page){ 
	 $(".con_duo").remove();
	 }
	})
	
})
function productgoodss(order_list){
	for(var i in order_list){
		order_list[i].order_recover="";
		order_list[i].order_delete="";
		order_list[i].order_state="";
		order_list[i].order_cancel="";
		 if(order_list[i].order_status==1){
			 order_list[i].order_state="已完成";
			 }else if(order_list[i].order_status==4){
			 order_list[i].order_state="退货"; 
			 }else if(order_list[i].order_status==2){	 
			 order_list[i].order_state="已取消"; 
			 order_list[i].order_recover="订单恢复"; 
			 order_list[i].order_delete="订单删除";
			 }else if(order_list[i].pay_status==0){
			 order_list[i].order_cancel="订单取消";
			 order_list[i].order_state="等待付款"; 	 
			 }else if((order_list[i].pay_status==2) && (order_list[i].shipping_status==4)){
			 order_list[i].order_state=="等待提货";
			 }else if((order_list[i].pay_status==2) && (order_list[i].shipping_status==1)){
			 order_list[i].order_state=="已发货"; 
			 }else if((order_list[i].pay_status==2) && (order_list[i].shipping_status==3)){
			 order_list[i].order_state=="退货中"; 
			 }else if(order_list[i].pay_status==2){
			 order_list[i].order_state=="已付款"; 
			 }	
		
	item = order_list[i];
	var str;
	if(typeof(str)=='undefined'){
		str='';
		}	
/*	str +='<div class="con_chan"><div class="chan_right"><p>订单编号：'+item.order_sn+'</p><p>金额：￥'+item.order_amount+'</p><p>下单日期：2013-12-15 16:16</p><p class="sate_order"><span>订单状态：</span><span class="con_color">'+item.order_state+'</span><a href="order_list.html?order_cancel='+item.order_id+'"><span class="order_cancel">'+item.order_cancel+'</span></a><a href="order_list.html?order_recover='+item.order_id+'"><span class="con_recover">'+item.order_recover+'</span></a><a href="order_list.html?order_delete='+item.order_id+'"><span class="con_delete">'+item.order_delete+'</span></a><a href="order_details.html?order_id='+item.order_id+'"><span class="con_biao" >查看详情</span></a></p></div></div>';*/

	if((item.order_cancel=='') && (item.order_recover=='') && (item.order_delete=='')){
		str +='<div class="con_chan"><div class="chan_right"><p>订单编号：'+item.order_sn+'</p><p>金额：￥'+item.order_amount+'</p><p>下单日期：<span class="order_time">'+item.add_time+'</span></p><p class="sate_order"><span>订单状态：</span><span class="con_color">'+item.order_state+'</span><a href="order_list.html?order_cancel='+item.order_id+'"><span   style="display:none" class="order_cancel">'+item.order_cancel+'</span></a><a href="order_list.html?order_recover='+item.order_id+'"><span style="display:none" class="con_recover">'+item.order_recover+'</span></a><a href="order_list.html?order_delete='+item.order_id+'"><span style="display:none" class="con_delete">'+item.order_delete+'</span></a><a href="order_details.html?order_id='+item.order_id+'"><span class="con_biao" >查看详情</span></a></p></div></div>';	
		}else if(item.order_delete==''){
	str +='<div class="con_chan"><div class="chan_right"><p>订单编号：'+item.order_sn+'</p><p>金额：￥'+item.order_amount+'</p><p>下单日期：<span class="order_time">'+item.add_time+'</span></p><p class="sate_order"><span>订单状态：</span><span class="con_color">'+item.order_state+'</span><a href="order_list.html?order_cancel='+item.order_id+'"><span  class="order_cancel">'+item.order_cancel+'</span></a><a href="order_list.html?order_recover='+item.order_id+'"><span style="display:none" class="con_recover">'+item.order_recover+'</span></a><a href="order_list.html?order_delete='+item.order_id+'"><span style="display:none" class="con_delete">'+item.order_delete+'</span></a><a href="order_details.html?order_id='+item.order_id+'"><span class="con_biao" >查看详情</span></a></p></div></div>';
	}else if(item.order_recover==''){
	str +='<div class="con_chan"><div class="chan_right"><p>订单编号：'+item.order_sn+'</p><p>金额：￥'+item.order_amount+'</p><p>下单日期：<span class="order_time">'+item.add_time+'</span></p><p class="sate_order"><span>订单状态：</span><span class="con_color">'+item.order_state+'</span><a href="order_list.html?order_cancel='+item.order_id+'"><span class="order_cancel">'+item.order_cancel+'</span></a><a href="order_list.html?order_recover='+item.order_id+'"><span style="display:none" class="con_recover">'+item.order_recover+'</span></a><a href="order_list.html?order_delete='+item.order_id+'"><span class="con_delete">'+item.order_delete+'</span></a><a href="order_details.html?order_id='+item.order_id+'"><span class="con_biao" >查看详情</span></a></p></div></div>';	
		
	}else if(item.order_cancel==''){
	str +='<div class="con_chan"><div class="chan_right"><p>订单编号：'+item.order_sn+'</p><p>金额：￥'+item.order_amount+'</p><p>下单日期：<span class="order_time">'+item.add_time+'</span></p><p class="sate_order"><span>订单状态：</span><span class="con_color">'+item.order_state+'</span><a href="order_list.html?order_cancel='+item.order_id+'"><span   style="display:none" class="order_cancel">'+item.order_cancel+'</span></a><a href="order_list.html?order_recover='+item.order_id+'"><span class="con_recover">'+item.order_recover+'</span></a><a href="order_list.html?order_delete='+item.order_id+'"><span class="con_delete">'+item.order_delete+'</span></a><a href="order_details.html?order_id='+item.order_id+'"><span class="con_biao" >查看详情</span></a></p></div></div>';	
	}}
	
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
var sArgName='order_delete';
var order_id=GetArgsFromHref(sHref,sArgName)
var sArgName='order_recover';
var order_recover=GetArgsFromHref(sHref,sArgName)
var sArgName='order_cancel';
var order_cancel=GetArgsFromHref(sHref,sArgName)
Orderlists.OrderlistsRoute = Ember.Route.extend({
  model: function () {
	 if(is_login){
		var login=1;
	}else{
		var login=0;
	 }
	 var user_val={'user_id':user_content.user_id,'is_login':login}
	 user_info = get_ws_data('get_user_info',{a:user_val}); //会员信息
	  if(order_id != ''){
	 order_d = get_ws_data('delete_order',{a:user_content.user_id,b:order_id}); //订单删除
	  }
	  if(order_recover != ''){
	 order_d = get_ws_data('recover_order',{a:user_content.user_id,b:order_recover}); //订单订单恢复
	  }
	  if(order_cancel != ''){
	 order_d = get_ws_data('cancel_order',{a:user_content.user_id,b:order_cancel}); //订单取消
	  }
	 order_list = get_ws_data('order_list',{a:user_content.user_id,b:'',c:0,d:size,e:page}); //订单列表
	 order_num = get_ws_data('order_num',{a:user_content.user_id,b:'',c:0}); //会员信息
	var list=[];
	 for(var i in order_list){
		 if(order_list[i].order_status==1){
			 order_list[i].order_state="已完成";
			 }else if(order_list[i].order_status==4){
			 order_list[i].order_state="退货"; 
			 }else if(order_list[i].order_status==2){	 
			 order_list[i].order_state="已取消"; 
			 order_list[i].order_recover="订单恢复"; 
			 order_list[i].order_delete="订单删除";
			 }else if(order_list[i].pay_status==0){
			 order_list[i].order_cancel="订单取消";
			 order_list[i].order_state="等待付款"; 	 
			 }else if((order_list[i].pay_status==2) && (order_list[i].shipping_status==4)){
			 order_list[i].order_state=="等待提货";
			 }else if((order_list[i].pay_status==2) && (order_list[i].shipping_status==1)){
			 order_list[i].order_state=="已发货"; 
			 }else if((order_list[i].pay_status==2) && (order_list[i].shipping_status==3)){
			 order_list[i].order_state=="退货中"; 
			 }else if(order_list[i].pay_status==2){
			 order_list[i].order_state=="已付款"; 
			 }
		list.push(order_list[i]);
		 }
		


	 console.log(order_list);
	 // goods_name=decodeURI(promise.goods_name);
	 // alert(goods_name);
	 // promise.goods_name=decodeURI(promise.goods_name);
	 var context ={};
	 context.userinfo = user_info;
	 context.ordernum = order_num;
	 context.orderlist = list;
	 context.islogin = is_login;
	 
	
	 return context;
  }
  
});


Orderlists.Orderlist = DS.Model.extend({
  goods_name: DS.attr('string'),
  shop_price: DS.attr('string'),
  promote_price: DS.attr('string'),
  salesvol: DS.attr('string'),
  goods_thumb: DS.attr('string'),
  isCompleted: DS.attr('boolean')
});





