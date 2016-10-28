
function PartyPageController(partyAPIService) {
	const ctrl = this;

	function getParties() {
		partyAPIService.parties.get().$promise.then((data) => {
			ctrl.parties = data.results;
		});
	};

	getParties();

}

export default PartyPageController;