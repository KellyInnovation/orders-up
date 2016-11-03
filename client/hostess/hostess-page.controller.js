
function HostessPageController(hostessAPIService) {
	const ctrl = this;
	ctrl.editedParty = {};

	function getParties() {
		hostessAPIService.parties.get().$promise.then((data) => {
			ctrl.parties = data.results;
		});
	};

	getParties();	

	ctrl.saveParty = function saveParty(editedParty) {
		hostessAPIService.hostess.save(editedParty).$promise.then((savedParty) => {
			ctrl.hostess = [
				savedParty,
					ctrl.hostess,
			];
			ctrl.editedParty = {};
			alert('Party added');
		});
	};

}

export default HostessPageController;