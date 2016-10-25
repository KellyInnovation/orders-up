import template from './hostess-seating.html';

import HostessSeatingController from './hostess-seating.controller';

const hostessSeatingComponent = {
	template,
	bindings: {
		party: '<',
	},
	controller: HostessSeatingController,
	controllerAs: 'hostessSeatingCtrl',
};

export default hostessSeatingComponent;