
$(function(){
		var products_foot;
		products_foot='<div style="height:5px; background:#fff;"></div><div class="foot_content"><div class="foot_home"><a href="../index.php" id="font_red">首页</a></div><div class="foot_sc"><a href="../users/collection_list.html">收藏</a></div><div class="foot_buy"><a href="../order/shopping_cart.html">购物车</a></div><div class="foot_user"><a href="../users/usercenter.html">我的华尔</a></div></div>'
      $("#foot_products").append(products_foot)
	  
	  	var user_foot;
		user_foot='<div style="height:5px; background:#fff;"></div><div class="foot_content"><div class="foot_home"><a href="../index.php" id="font_red">首页</a></div><div class="foot_sc"><a href="./users/collection_list.html">收藏</a></div><div class="foot_buy"><a href="../order/shopping_cart.html">购物车</a></div><div class="foot_user"><a href="./users/usercenter.html">我的华尔</a></div></div>'
      $("#foot_users").append(user_foot)
	  
	  	var order_foot;
		order_foot='<div style="height:5px; background:#fff;"></div><div class="foot_content"><div class="foot_home"><a href="../index.php" id="font_red">首页</a></div><div class="foot_sc"><a href="../users/collection_list.html">收藏</a></div><div class="foot_buy"><a href="./order/shopping_cart.html">购物车</a></div><div class="foot_user"><a href="../users/usercenter.html">我的华尔</a></div></div>'
      $("#foot_order").append(order_foot)
})