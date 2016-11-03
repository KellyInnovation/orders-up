
function KitchenFormController() {
	const ctrl = this;
	ctrl.editedMenu = {};

	ctrl.saveMenuItem = function saveMenuItem(editedMenu) {
		kitchenAPIService.menus.save(editedMenu).$promise.then((editedMenu) => {
			ctrl.menus = [
				savedMenu,
					ctrl.menus,
			];
			ctrl.editedMenu = {};
			alert("added")
		})
	};
}

export default KitchenFormController;