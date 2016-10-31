
function partyAPIService($resource) {
	const api = {
		parties: $resource('/api/party/:id',
			{ id: '@id'},
		),
	};

	return api;
}

export default partyAPIService;