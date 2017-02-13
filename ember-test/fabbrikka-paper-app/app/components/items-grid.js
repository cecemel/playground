import Ember from 'ember';

export default Ember.Component.extend({

	_formatRows: function(data){
		let rows = [], size = 3;
		while (data.length > 0){
			rows.push(data.splice(0, size))
		}
		return rows
	},

	init(){
		this._super(...arguments);
		this.set("rows", this._formatRows(this.get('data')));
	}
});
