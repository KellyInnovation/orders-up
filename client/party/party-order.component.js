import template from './party-order.html';

import PartyOrderController from './party-order.controller';

const partyOrderComponent = {
	template,
	bindings: {
		party: '<',
		order: '<',
		update: '&',
	},
	controller: PartyOrderController,
	controllerAs: 'partyOrderCtrl',
};

export default partyOrderComponent;