
function HostessPageController(hostessAPIService, partyAPIService) {
	const ctrl = this;
	ctrl.editedParty = {};

	function getHostessParties() {
		hostessAPIService.hostess.get().$promise.then((data) => {
			ctrl.hostess = data.results;
		});

	};

	getHostessParties();	

	function getParty() {
		partyAPIService.parties.get().$promise.then((data) => {
			ctrl.parties = data.results;

		});
	};

	getParty();

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
			getHostessParties();
		});
	};

	ctrl.deleteParty = function deleteParty(partyToDelete) {
		const findParty = findIndex(item => partyToDelete.id === item.id);
		const index = findParty(ctrl.hostess);

		if (index !== -1) {
			ctrl.hostess.splice(index, 1);
		}

		hostessAPIService.hostess.delete(partyToDelete).$promise.then(() => {
			alert('deleted')
		});
	};

}

export default HostessPageController;