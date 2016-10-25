import template from './hostess-checkin.html';

import HostessCheckinController from './hostess-checkin.controller';

const hostessCheckinComponent = {
	template,
	bindings: {
		party: '<',
		save: '&',
	},
	controller: HostessCheckinController,
	controllerAs: 'hostessCheckinCtrl',
};

export default hostessCheckinComponent;