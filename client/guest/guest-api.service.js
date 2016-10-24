
function guestAPIService($resource) {
	const api = {
		guests: $resource('/api/guest/:id',
			{ id: '@id' },
		),

	};

	return api;
}

export default guestAPIService;