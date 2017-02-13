import Ember from 'ember';

export default Ember.Route.extend({
	model(params) {
		return {
	  		name: "sesame abierte",
	  		price: "89$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/1/details/1.jpg",
	  		altName: "nice thing look here",
	  		images:["http://playground.ruizdearcaute.com:9090/images/1/details/1.jpg"
	  		, "http://playground.ruizdearcaute.com:9090/images/1/details/2.jpg"
	  		, "http://playground.ruizdearcaute.com:9090/images/1/details/3.jpg"]
	  	}
	},
});
