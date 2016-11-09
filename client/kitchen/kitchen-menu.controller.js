
function KitchenMenuController($stateParams, partyAPIService) {
	const ctrl = this;
	ctrl.foodOrder = {};

	ctrl.addFood = function addFood(foodOrder) {
		console.log("run save order")
		console.log(ctrl.foodOrder)
		partyAPIService.parties.update(foodOrder).$promise.then((savedFood) => {
			ctrl.parties = [
				savedFood,
					ctrl.parties,
			];
			// ctrl.foodOrder = {};
		});
	};


}

export default KitchenMenuController;