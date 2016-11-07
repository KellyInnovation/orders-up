
function KitchenController(kitchenAPIService) {
	const ctrl = this;
	ctrl.editedMenu = {};
	ctrl.foodToOrder = {};

	function getOrders() {
		kitchenAPIService.menus.get().$promise.then((data) => {
			ctrl.menus = data.results;
		});
	};

	getOrders();

	ctrl.saveMenu = function saveMenu(editedMenu) {
		kitchenAPIService.menus.save(editedMenu).$promise.then((savedMenu) => {
			ctrl.menus = [
				savedMenu,
					ctrl.menus,
			];
			ctrl.editedMenu = {};
			getMenus();
		});
	};

	ctrl.saveOrder = function saveOrder(foodToOrder) {
		const findFood = findIndex(item => foodToOrder.id === item.id);
		const index = findFood(ctrl.menus);

		if (index !== -1) {
			kitchenAPIService.menus.orders.save(foodToOrder).$promise.then((savedFood) => {
				ctrl.menus.orders = [
					savedFood, 
						ctrl.item,
				];
				ctrl.foodToOrder = {};

			});
		};
		alert('called');
	};

}

export default KitchenController;