import Ember from 'ember';

export default Ember.Controller.extend({

  isDisabled: Ember.computed.not('isValid'),
  isValid: Ember.computed.and('isValidEmail', 'isValidText'),

  isValidEmail: Ember.computed.match('model.email', /^.+@.+\..+$/),
  isValidText: Ember.computed.gte('model.message.length', 5),

});