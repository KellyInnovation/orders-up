
function KitchenController(kitchenAPIService) {
	const ctrl = this;

	function getMenus() {
		kitchenAPIService.menus.get().$promise.then((data) => {
			ctrl.menus = data.results;
		});
	};

	getMenus();
}

export default KitchenController;