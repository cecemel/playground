import DS from 'ember-data';

export default DS.Model.extend({
	 name: DS.attr(),
	 price: DS.attr(),
	 mainImage: DS.attr(),
	 altName: DS.attr()
});
