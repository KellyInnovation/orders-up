import template from './hostess-page.html';

import HostessPageController from './hostess-page.controller';

const hostessPageComponent = {
	template,
	bindings: {
		hostess: '<',
	},
	controller: HostessPageController,
	controllerAs: 'hostessPageCtrl',
};

export default hostessPageComponent;