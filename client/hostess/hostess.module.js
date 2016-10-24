import angular from 'angular';
import 'angular-resource';
import 'angular-filter';

import hostessPageComponent from './hostess-page.component';

import hostessAPIService from './hostess-api.service';

const HostessModule = angular.module(
	'parties', [
	'ngResource',
	'angular.filter',
])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	})
	.factory('hostessAPIService', hostessAPIService)
	.component('hostessPage', hostessPageComponent);

export default HostessModule;