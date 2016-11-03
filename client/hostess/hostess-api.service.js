
function hostessAPIService($resource) {
	const api = {
		parties: $resource('/api/hostess/:id',
			{ id: '@id' },
			{
				update: {
					method: 'PUT',
				},
			},
		),
	};

	return api;
}

export default hostessAPIService;