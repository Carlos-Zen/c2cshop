// JavaScript Document
window.Todos = Ember.Application.create();

Todos.ApplicationAdapter = DS.FixtureAdapter.extend();

Todos.Router.map(function () {
  this.resource('todos', { path: '/' });
});

Todos.TodosRoute = Ember.Route.extend({
  model: function () {
    return this.store.find('todo');
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


Todos.Todo.FIXTURES = [
  {
    id: 1,
    goods_name: '2013冬新款防水台真皮女靴两穿靴高跟靴短靴女坡跟厚底粗跟雪地靴',
	goods_thumb:'img/xq.jpg',
	shop_price:'885',
	promote_price:'665',
	salesvol:'8524',
    isCompleted: true
  }
];



