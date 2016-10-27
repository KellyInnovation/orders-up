import template from './kitchen-food-modal.html';

import KitchenFoodModalController from './kitchen-food-modal.controller';

const kitchenFoodModalComponent = {
	template,
	bindings: {
		resolve: '<',
		close: '&',
		dismiss: '&'
	},
	controller: KitchenFoodModalController,
	controllerAs: 'kitchenFoodModalCtrl',
};

export default kitchenFoodModalComponent;