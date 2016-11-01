
function partyAPIService($resource) {
	const partyResource = $resource('/api/party/:id/',
			{ id: '@id'},
		);
	return {
		getAllParties() {
			return partyResource.get({}).$promise.then((data) => { 
				return data.results;
			});
		},
		getParty(id) {
			return partyResource.get({ id }).$promise.then((data) => {
				return data;
			});
		},
	};

}

export default partyAPIService;