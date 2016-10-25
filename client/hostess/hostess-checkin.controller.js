
function HostessCheckinController() {
	const ctrl = this;
	ctrl.editedParty = {};

	ctrl.addParty = function addParty() {
		ctrl.save({ editedParty: ctrl.editedParty });
	};
}

export default HostessCheckinController;