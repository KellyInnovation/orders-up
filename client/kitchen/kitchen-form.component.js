import template from './kitchen-form.html';

import KitchenFormController from './kitchen-form.controller';

const kitchenFormComponent = {
	template,
	bindings: {
		menu_setting: '<',
		save: '&',
	},
	controller: KitchenFormController,
	controllerAs: 'kitchenFormCtrl',
};

export default kitchenFormComponent;