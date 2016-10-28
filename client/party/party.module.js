import angular from 'angular';
import 'angular-resource';


import partyPageComponent from './party-page.component';

import partyAPIService from './party-api.service';

const PartyModule = angular.module(
	'parties', [
	'ngResource',


])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	}) 
	.factory('partyAPIService', partyAPIService)
	.component('partyPage', partyPageComponent);

export default PartyModule;