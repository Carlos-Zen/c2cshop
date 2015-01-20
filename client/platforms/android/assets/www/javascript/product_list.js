window.Product = Ember.Application.create();

Product.ApplicationAdapter = DS.FixtureAdapter.extend();

Product.Router.map(function () {
  this.resource('product', { path: '/' });
});

Product.ProductRoute = Ember.Route.extend({
  model: function () {
    return this.store.find('goods');
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


//团购专区列表商品参数，还有时间参数
Product.Goods.FIXTURES = [
  {
    id: 1,
    goods_name: '2013冬新款防水粗跟雪地靴',
	goods_thumb:'img/lb1.jpg',
	shop_price:'885',
	promote_price:'665',
	salesvol:'8524',
	discount:'8.8',
	start_time:'1391823191',
	end_time:'1400809191',
    isCompleted: true
  },
  {
    id: 2,
    goods_name: '大容量移动USB输出充电宝',
	goods_thumb:'img/lb1.jpg',
	shop_price:'885',
	promote_price:'665',
	salesvol:'8524',
	discount:'6.6',
	start_time:'1391823191',
	end_time:'1400009191',
    isCompleted: true
  },
  {
    id: 3,
    goods_name: '双出充电宝值得拥有',
	goods_thumb:'img/lb1.jpg',
	shop_price:'885',
	promote_price:'665',
	salesvol:'8524',
	discount:'4.4',
	start_time:'1391823191',
	end_time:'1401099191',
    isCompleted: true
  }
];
