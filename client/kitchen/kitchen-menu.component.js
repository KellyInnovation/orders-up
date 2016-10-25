import template from './kitchen-menu.html';

import KitchenMenuController from './kitchen-menu.controller';

const kitchenMenuComponent = {
	template,
	bindings: {
		item: '<',
	},
	controller: KitchenMenuController,
	controllerAs: 'kitchenMenuCtrl',
};

export default kitchenMenuComponent;