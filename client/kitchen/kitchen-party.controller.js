

function KitchenPartyController(kitchenAPIService) {
	const ctrl = this;
	ctrl.editedMenu = {};
	ctrl.foodToOrder = {};

	function getMenus() {
		kitchenAPIService.menus.get().$promise.then((data) => {
			ctrl.menus = data.results;
		});
	};

	getMenus();

	// ctrl.saveOrder = function saveOrder(foodToOrder) {
	// 	console.log('party')
	// 	kitchenAPIService.menus.orders.save(foodToOrder).$promise.then((savedFood) => {
	// 			ctrl.menus.orders = [
	// 				savedFood, 
	// 					ctrl.item,
	// 			];
	// 			ctrl.foodToOrder = {};

	// 		});
	// };

}

export default KitchenPartyController;
	
