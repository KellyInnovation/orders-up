
function KitchenFormController() {
	const ctrl = this;
	ctrl.editedMenuSetting = {};

	ctrl.addMenuSetting = function addMenuSetting() {
		ctrl.save({ editedMenuSetting: ctrl.editedMenuSetting });
	};
}

export default KitchenFormController;