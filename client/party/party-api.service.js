
function partyAPIService($resource) {
	const partyResource = {
		parties: $resource('/api/party_order/:id',
			{ id: '@id' },
		),

	};

	return api;
}

export default partyAPIService;