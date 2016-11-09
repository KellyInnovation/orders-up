
function partyAPIService($resource) {
	const api = {
		parties: $resource('/api/party/:id/',
			{ id: '@id'},
			{
				update: {
					method: 'PUT',
				},
			}),
		
	};

	return api;

}

export default partyAPIService;