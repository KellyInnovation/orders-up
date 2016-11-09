
function HostessSeatingController(partyAPIService) {
	const ctrl = this;

	ctrl.deleteParty = function deleteParty() {
		ctrl.delete({ partyToDelete: ctrl.party });
	}


}

export default HostessSeatingController;