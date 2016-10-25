
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
		hostessAPIService.parties.save(editedParty).$promise.then((savedParty) => {
			ctrl.parties = [
				savedParty,
					ctrl.party,
			];
			ctrl.editedParty = {};
			alert("party added")
		}); 
	};
}

export default HostessPageController;