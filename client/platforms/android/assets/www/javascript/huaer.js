window.Huaer = Ember.Application.create();

Huaer.ApplicationAdapter = DS.FixtureAdapter.extend();

Huaer.Router.map(function () {
  this.resource('huaer', { path: '/' });
});

Huaer.HuaerRoute = Ember.Route.extend({
  model: function () {
    return this.store.find('group');
  }
});

Huaer.Group = DS.Model.extend({
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


//首页团购专区列表商品参数
Huaer.Group.FIXTURES = [
  {
    id: 1,
    goods_name: 'NB经典复古跑步鞋',
	goods_thumb:'img/t2.jpg',
	shop_price:'218',
	promote_price:'198',
	salesvol:'8524',
	discount:'8.8',
	start_time:'1391823191',
	end_time:'1400809191',
    isCompleted: true
  },
  {
    id: 2,
    goods_name: 'DILAKS真皮女包手提包',
	goods_thumb:'img/t1.jpg',
	shop_price:'218',
	promote_price:'198',
	salesvol:'8524',
	discount:'6.6',
	start_time:'1391823191',
	end_time:'1400009191',
    isCompleted: true
  },
  {
    id: 3,
    goods_name: '莱卡锥腿男牛仔裤',
	goods_thumb:'img/t3.jpg',
	shop_price:'885',
	promote_price:'665',
	salesvol:'8524',
	discount:'4.4',
	start_time:'1391823191',
	end_time:'1401099191',
    isCompleted: true
  },
  {
    id: 4,
    goods_name: 'KISSCAT方跟浅口女单鞋',
	goods_thumb:'img/t4.jpg',
	shop_price:'885',
	promote_price:'665',
	salesvol:'8524',
	discount:'4.4',
	start_time:'1391823191',
	end_time:'1401099191',
    isCompleted: true
  }
];
