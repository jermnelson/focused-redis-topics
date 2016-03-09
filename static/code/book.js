/* Sample Book Sales by Jeremy Nelson */
var nohm = require('nohm').Nohm;
var redis = require('redis').createClient();

nohm.setClient(redis);
nohm.setPrefix('catalog'); 

nohm.model('Book', {
	  properties: {
			          title: {
						       type: 'string',
	      unique: false,
	      validations: [
	        'notEmpty'
	      ]
	    },
	    author: {
			          type: 'string',
	      unique: false
	    },
	    price: {
			         type: 'integer',
	      defaultValue: 20
	    }
 }
});

nohm.model('Sales', {
	  properties: {
			          salesDate: {
						           type: 'datetime'
	    }
					       }
});

var infiniteJest = nohm.factory('Book');
var bookSales = nohm.factory('Sales');


infiniteJest.p({
	  title: 'Infinite Jest',
	  author: 'David Foster Wallace',
	  price: 20
});

bookSales.p({
	  salesDate: '2016-03-09'
});

bookSales.link(infiniteJest, 'item');

infiniteJest.save();
bookSales.save();
