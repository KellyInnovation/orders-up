
function KitchenMenuController() {
	const ctrl = this;
	ctrl.foodToOrder = {};

	ctrl.saveOrder = function saveOrder(foodToOrder) {
		ctrl.save({ foodToOrder: ctrl.foodToOrder });
	};


}

export default KitchenMenuController;