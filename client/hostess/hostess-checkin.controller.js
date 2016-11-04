import { merge } from 'ramda';

function HostessCheckinController() {
	const ctrl = this;
	ctrl.editedParty = {};

	ctrl.$onChanges = function $onChanges() {
		ctrl.editedParty = merge({}, ctrl.hostess);
	};

	ctrl.saveParty = function saveParty() {
		ctrl.save({ editedParty: ctrl.editedParty });
	};
}

export default HostessCheckinController;