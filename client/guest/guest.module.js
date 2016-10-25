import angular from 'angular';
import 'angular-resource';
import 'angular-filter';

import guestPageComponent from './guest-page.component';
import guestMenuComponent from './guest-menu.component';

import guestAPIService from './guest-api.service';

const GuestModule = angular.module(
	'guests', [
	'ngResource',
	'angular.filter',
])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	}) 
	.factory('guestAPIService', guestAPIService)
	.component('guestPage', guestPageComponent)
	.component('guestMenu', guestMenuComponent);

export default GuestModule;