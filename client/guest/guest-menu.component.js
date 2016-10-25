import template from './guest-menu.html';

import GuestMenuController from './guest-menu.controller';

const guestMenuComponent = {
	template,
	bindings: {
		guest: '<',
	},
	controller: GuestMenuController,
	controllerAs: 'guestMenuCtrl',
};

export default guestMenuComponent;