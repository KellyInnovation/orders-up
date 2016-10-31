import template from './party-page.html';

import PartyPageController from './party-page.controller';

const partyPageComponent = {
	template,
	bindings: {
		parties: '<',
	},
	controller: PartyPageController,
	controllerAs: 'partyPageCtrl',
};

export default partyPageComponent;