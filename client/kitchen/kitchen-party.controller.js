

function KitchenPartyController(kitchenAPIService) {
	const ctrl = this;
	ctrl.editedMenu = {};

	function getMenus() {
		kitchenAPIService.menus.get().$promise.then((data) => {
			ctrl.menus = data.results;
		});
	};

	getMenus();

}

export default KitchenPartyController;
	
