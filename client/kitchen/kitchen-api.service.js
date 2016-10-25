
function kitchenAPIService($resource) {
	const api = {
		menus: $resource('/api/kitchen/:id',
			{ id: '@id'},
		),
	};

	return api;
}

export default kitchenAPIService;