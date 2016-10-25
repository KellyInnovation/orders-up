
function GuestPageController(guestAPIService ) {
	const ctrl = this;

	function getGuests() {
		guestAPIService.guests.get().$promise.then((data) => {
			ctrl.guests = data.results;
		});
	};

	getGuests();

}

export default GuestPageController;