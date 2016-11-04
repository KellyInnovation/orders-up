
function KitchenController(kitchenAPIService) {
	const ctrl = this;
	ctrl.editedMenu = {};

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

}

export default KitchenController;