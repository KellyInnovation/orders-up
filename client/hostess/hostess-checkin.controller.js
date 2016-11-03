
function HostessCheckinController() {
	const ctrl = this;
	ctrl.editedParty = {};

	ctrl.saveParty = function saveParty() {
		ctrl.save({ editedParty: ctrl.editedParty });
	};
}

export default HostessCheckinController;