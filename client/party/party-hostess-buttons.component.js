import template from './party-hostess-buttons.html';

import PartyHostessButtonsController from './party-hostess-buttons.controller';

const partyHostessButtonsComponent = {
	template,
	bindings: {
		party: '<',
		host: '<',
	},
	controller: PartyHostessButtonsController,
	controllerAs: 'partyHostessButtonsCtrl',
};

export default partyHostessButtonsComponent;