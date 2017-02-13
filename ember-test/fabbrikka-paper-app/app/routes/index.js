import Ember from 'ember';

export default Ember.Route.extend({
	  model() {
	  	return [{
	  		name: "nice thingy",
	  		price: "57$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/1/1.jpg",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "romantic shirt",
	  		price: "64$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/2/2.jpg",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "sesame abierte",
	  		price: "89$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/3/3.jpg",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "bla waw",
	  		price: "60$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/4/4.jpg",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "tchik tchas",
	  		price: "99$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/5/5.jpg",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "jadad",
	  		price: "45$",
	  		mainImage: "http://playground.ruizdearcaute.com:9090/images/6/6.jpg",
	  		altName: "nice thing look here"
	  	}];
	  }
});