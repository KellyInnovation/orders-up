
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
			
		});
	};

}

export default KitchenController;