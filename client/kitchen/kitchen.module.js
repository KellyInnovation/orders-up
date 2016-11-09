import angular from 'angular';
import 'angular-resource';
import 'angular-filter';


import kitchenPageComponent from './kitchen-page.component';
import kitchenMenuComponent from './kitchen-menu.component';
import kitchenPartyComponent from './kitchen-party.component';
import kitchenFormComponent from './kitchen-form.component';
import kitchenOrderComponent from './kitchen-order.component';

import partyPageComponent from '../party/party-page.component';

import kitchenAPIService from './kitchen-api.service';
import partyAPIService from '../party/party-api.service';


const KitchenModule = angular.module('menus', [
	'ngResource',
	'angular.filter',

])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	})
	.factory('kitchenAPIService', kitchenAPIService)
	.factory('partyAPIService', partyAPIService)
	.component('kitchenPage', kitchenPageComponent)
	.component('kitchenMenu', kitchenMenuComponent)
	.component('kitchenParty', kitchenPartyComponent)
	.component('kitchenForm', kitchenFormComponent)
	.component('kitchenOrder', kitchenOrderComponent);

export default KitchenModule;