
function hostessAPIService($resource) {

	const api = {
		hostess: $resource('/api/hostess/:id',
			{ id: '@id' },
			{
				update: {
					method: 'PUT',
				},
			}),
	};

	return api;
}

export default hostessAPIService;

	// const hostessResource = $resource('/api/hostess/:id/', 
	// 	{ id: '@id' });

	// return {
	// 	getAllHostess() {
	// 		return hostessResource.get({}).$promise.then((data) => {
	// 			return data.results;
	// 		});
	// 	},
	// 	getHostess(id) {
	// 		return hostessResource.get({id}).$promise.then((data) => {
	// 			return data;
	// 		});
	// 	},
	// 	createHostess() {
	// 		const create = hostessResource.post({
	// 			url: '/api/hostess/post/',

	// 		})
	// 	}
		// createParty() {
		// 	return 
		// }
	// }