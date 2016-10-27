
function KitchenFoodModalController() {
	const ctrl = this;

	ctrl.$onInit = function $onInit() {
		ctrl.items = ctrl.resolve.items;
		ctrl.selected = {
			item: ctrl.items[0]
		};
	};

	ctrl.close = function close() {
		ctrl.dismiss({$value: 'cancel'});
	};
}

export default KitchenFoodModalController;