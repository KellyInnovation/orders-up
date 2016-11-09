
function PartyOrderController($stateParams) {
	const ctrl = this;
	ctrl.foodOrder = {food: ctrl.order, id: $stateParams.partyId};

	ctrl.addFood = function addFood(foodOrder) {
		// ctrl.foodOrder.push($stateParams.hostessId)
		console.log($stateParams.partyId)
		console.log(ctrl.foodOrder);
		ctrl.update({ foodOrder: ctrl.foodOrder });
		// console.log("order party food");
	};
}

export default PartyOrderController;