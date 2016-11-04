
function HostessPageController(hostessAPIService) {
	const ctrl = this;
	ctrl.editedParty = {};

	function getParties() {
		hostessAPIService.hostess.get().$promise.then((data) => {
			ctrl.hostess = data.results;
		});
	};

	getParties();	

	ctrl.saveParty = function saveParty(editedParty) {
		hostessAPIService.hostess.save(editedParty).$promise.then((savedParty) => {
			ctrl.hostess = [
				savedParty,
					ctrl.hostess,
			];
			ctrl.createParty = function createParty(partyAPIService) {
				partyAPIService.parties.save(editedParty).$promise.then((savedParty) => {
					ctrl.parties = [
						savedParty,
							ctrl.parties,
					];
				});
			};
			ctrl.editedParty = {};
			getParties();
		});
	};

}

export default HostessPageController;