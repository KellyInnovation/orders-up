
function KitchenMenuController($stateParams, partyAPIService) {
	const ctrl = this;
	ctrl.foodOrder = {};

	ctrl.addFood = function addFood(foodOrder, $stateParams) {
		
		console.log("run save order")
		console.log(ctrl.foodOrder)
		partyAPIService.parties.update(foodOrder).$promise.then(() => {
			
			// ctrl.foodOrder = {};
		});
	};


}

export default KitchenMenuController;