//������������Ա�������䣬�Ƴ�Ԫ��
Array.prototype.remove=function(dx)
{
    if(isNaN(dx)||dx>this.length){
        return false;
    }
    for(var i=0,n=0;i<this.length;i++)
    {
        if(this[i]!=this[dx])
        {
            this[n++]=this[i]
        }
    }
    this.length-=1
}
            
            
//���ﳵ�ඨ��
cart = function(){
    this.lstore = window.localStorage;
    this.init();
	
};
cart.prototype={
    init:function(){
        var cart_goods_material=this.lstore.getItem('cart');
        try{
            this.cart_goods=JSON.parse(cart_goods_material);
			if(this.cart_goods==null)
				this.cart_goods=[];
        }
        catch(e){
            this.cart_goods=[];
        }
    },
    addgetall:function(){                   //��¼ǰ��ù��ﳵ������Ʒ�б�

        return this.cart_goods;
		
    },
    getall:function(){                   //��ù��ﳵ������Ʒ�б�
		if(!(is_login)){
        return this.cart_goods;
		}else{
			//��½�����
			var user_content=ath.get_userinfo();
			var user_id={'user_id':user_content.user_id}
			cart_goods = get_ws_data('cart_get',{a:user_id}); //��ȡ���ﳵ��Ʒ
			return cart_goods
		}
    },
    insert:function(goods){              //������Ʒ
		if(!(is_login)){
		try{
        var index=this.finds(goods.goods_id);
		}catch(e){
			var index = -1;
			}
        if(index>-1){
            this.cart_goods[index].goods_number+=goods.goods_number;
        }else{
            this.cart_goods.push(goods);
                            
        }
        var cart_goods_cooked = JSON.stringify(this.cart_goods);
        this.lstore.setItem('cart',cart_goods_cooked);
        return true;
		}else{
			//��½�����
			var user_content=ath.get_userinfo();
			var goods= {'user_id':user_content.user_id,'goods_id':goods.goods_id,'goods_number':goods.goods_number}
			insert_goods = get_ws_data('cart_insert',{a:goods}); //���빺�ﳵ��Ʒ
			if(insert_goods.rst == 'ok'){
			//console.log(cart_goods.rst);
			return true
			}
			}
    },
    update:function(goods_id,data){
        var index=this.finds(goods_id);
        if(index>-1){
            for(var i in data){
                this.cart_goods[index][i]=data[i];
            }   
        }
        var cart_goods_cooked = JSON.stringify(this.cart_goods);
        this.lstore.setItem('cart',cart_goods_cooked);
        return true;
		
    },
    addnum:function(goods_id,num){      //���¹��ﳵ��Ʒ����
		if(!(is_login)){
        var index=this.finds(goods_id);
        var num=this.cart_goods[index]['goods_number']+num;
        this.update(goods_id,{
            'goods_number':num
        });   
		}else{
			//��½�����
			cart_goods = get_ws_data('cart_update',{a:goods_id,b:num}); //���ﳵ��Ʒ���ı�
			}
    },
    del:function(goods_id){ 
		if(!(is_login)){          
        var index=this.finds(goods_id);
        this.cart_goods.remove(index);
		var cart_goods_cooked = JSON.stringify(this.cart_goods);
        this.lstore.setItem('cart',cart_goods_cooked);
        return true;
		}else{
			//��½�����
			var del_goods={'rec_id':goods_id}
			cart_goods_del = get_ws_data('cart_delete',{a:del_goods}); //ɾ�����ﳵ��Ʒ
			return cart_goods_del.rs;
			
			}
	
    },
    finds:function(goods_id){
        var index=-1;
		if(this.cart_goods.length>0){
        for(var  i in this.cart_goods ){
            var g=this.cart_goods[i];
            if(g.goods_id==goods_id){
                index = i;
                break;
            }
        }}
        return index;
    },
    clear:function(){
        this.lstore.setItem('cart','');
		this.cart_goods=[];
    },
    amount:function(){
        var amount=0;
        for(var  i in this.cart_goods ){
            amount += this.cart_goods[i]['goods_number']*this.cart_goods[i]['goods_price'];
        }
        return amount;
    }
}