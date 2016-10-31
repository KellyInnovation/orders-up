import angular from 'angular';
import 'angular-resource';

import partyPageComponent from './party-page.component';

import partyAPIService from './party-api.service';

const PartyModule = angular.module(
	'parties', [
	'ngResource',

])
	.config(function($stateProvider) {
		var kitchenPageState = {
			name: 'kitchen-page',
			url: '/kitchen-page.html'
		}
		$stateProvider.state(kitchenPageState);
	})
	.factory('partyAPIService', partyAPIService)
	.component('partyPage', partyPageComponent);

export default PartyModule;