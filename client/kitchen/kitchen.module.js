import angular from 'angular';
import 'angular-resource';
import 'angular-filter';


import kitchenPageComponent from './kitchen-page.component';
import kitchenMenuComponent from './kitchen-menu.component';
import kitchenPartyComponent from './kitchen-party.component';
import kitchenFormComponent from './kitchen-form.component';

import kitchenAPIService from './kitchen-api.service';

const KitchenModule = angular.module('menus', [
	'ngResource',
	'angular.filter',

])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	})
	.factory('kitchenAPIService', kitchenAPIService)
	.component('kitchenPage', kitchenPageComponent)
	.component('kitchenMenu', kitchenMenuComponent)
	.component('kitchenParty', kitchenPartyComponent)
	.component('kitchenForm', kitchenFormComponent);

export default KitchenModule;