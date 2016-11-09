
function PartyPageController(partyAPIService ) {
	const ctrl = this;
	ctrl.editedOrder = {};

	function getParties() {
		partyAPIService.parties.get().$promise.then((data) => {
			ctrl.parties = data.results;
		});
	};

	getParties();

}

export default PartyPageController;