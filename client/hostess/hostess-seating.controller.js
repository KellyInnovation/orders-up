
function HostessSeatingController(partyAPIService) {
	const ctrl = this;

	ctrl.deleteParty = function deleteParty() {
		ctrl.delete({ partyToDelete: ctrl.party });
	}

	function getParty() {
		partyAPIService.parties.get().$promise.then((data) => {
			ctrl.parties = data.results;
			console.log("party")
		});
	};

	getParty();

}

export default HostessSeatingController;