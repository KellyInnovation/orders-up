import angular from 'angular';
import angularResource from 'angular-resource';
import 'angular-filter';

import partyPageComponent from './party-page.component';
import partyOrderComponent from './party-order.component';
import partyHostessButtonsComponent from './party-hostess-buttons.component';

import partyAPIService from './party-api.service';

const PartyModule = angular.module(
	'parties', [
	angularResource,
	'angular.filter',
])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	})
	.factory('partyAPIService', partyAPIService)
	.component('partyPage', partyPageComponent)
	.component('partyOrder', partyOrderComponent)
	.component('partyHostessButtons', partyHostessButtonsComponent);

export default PartyModule;