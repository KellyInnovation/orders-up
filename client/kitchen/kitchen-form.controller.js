
function KitchenFormController() {
	const ctrl = this;
	ctrl.editedMenu = {};

	ctrl.saveMenu = function saveMenu(editedMenu) {
		ctrl.save({ editedMenu: ctrl.editedMenu });
	};
}

export default KitchenFormController;