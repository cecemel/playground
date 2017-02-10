import Ember from 'ember';

export default Ember.Route.extend({
	  model() {
	  	return [{
	  		name: "nice thingy",
	  		price: "57$",
	  		mainImage: "https://firebasestorage.googleapis.com/v0/b/fabbrikka-app.appspot.com/o/sweater-1.jpg?alt=media&token=f9bc1500-a27c-41f8-97ea-07c94720853e",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "romantic shirt",
	  		price: "64$",
	  		mainImage: "https://firebasestorage.googleapis.com/v0/b/fabbrikka-app.appspot.com/o/sweater-6.jpg?alt=media&token=6601d2cd-9665-4c4d-8306-f34abe7bab12",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "sesame abierte",
	  		price: "89$",
	  		mainImage: "https://firebasestorage.googleapis.com/v0/b/fabbrikka-app.appspot.com/o/sweater-5.jpg?alt=media&token=dcebbc05-402b-4080-b6d7-8f631fe3d99e",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "bla waw",
	  		price: "60$",
	  		mainImage: "https://firebasestorage.googleapis.com/v0/b/fabbrikka-app.appspot.com/o/sweater-4.jpg?alt=media&token=ebc0dcad-76e0-4e26-acbe-a67f2b8122dc",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "tchik tchas",
	  		price: "99$",
	  		mainImage: "https://firebasestorage.googleapis.com/v0/b/fabbrikka-app.appspot.com/o/sweater-5.jpg?alt=media&token=dcebbc05-402b-4080-b6d7-8f631fe3d99e",
	  		altName: "nice thing look here"
	  	},
	  	{
	  		name: "jadad",
	  		price: "45$",
	  		mainImage: "https://firebasestorage.googleapis.com/v0/b/fabbrikka-app.appspot.com/o/sweater-7.jpg?alt=media&token=121bbab8-83d9-4730-b11c-2c3268c7812f",
	  		altName: "nice thing look here"
	  	}];
	  }
});