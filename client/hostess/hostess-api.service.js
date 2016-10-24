
function hostessAPIService($resource) {
	const api = {
		parties: $resource('/api/hostess/:id',
			{ id: '@id' },
		),
	};

	return api;
}

export default hostessAPIService;