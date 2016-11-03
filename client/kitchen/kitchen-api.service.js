
function kitchenAPIService($resource) {
	const api = {
		menus: $resource('/api/kitchen/:id',
			{ id: '@id'},
			{
				update: {
					method: 'PUT',
				},
			},
		),
	};

	return api;
}

export default kitchenAPIService;