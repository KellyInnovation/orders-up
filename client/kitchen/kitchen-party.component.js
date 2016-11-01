import template from './kitchen-party.html';

import KitchenPartyController from './kitchen-party.controller';

const kitchenPartyComponent = {
	template,
	controller: KitchenPartyController,
	controllerAs: 'kitchenPartyCtrl',
};

export default kitchenPartyComponent;