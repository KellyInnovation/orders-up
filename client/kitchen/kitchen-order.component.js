import template from './kitchen-order.html';

import KitchenOrderController from './kitchen-order.controller';

const kitchenOrderComponent = {
	template,
	bindings: {
		menu: '<',
	},
	controller: KitchenOrderController,
	controllerAs: 'kitchenOrderCtrl',
};

export default kitchenOrderComponent;