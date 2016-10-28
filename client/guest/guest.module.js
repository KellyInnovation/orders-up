import angular from 'angular';
import 'angular-resource';


import guestPageComponent from './guest-page.component';

import guestAPIService from './guest-api.service';

const GuestModule = angular.module(
	'guests', [
	'ngResource',


])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	}) 
	.factory('guestAPIService', guestAPIService)
	.component('guestPage', guestPageComponent);

export default GuestModule;