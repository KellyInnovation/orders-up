import angular from 'angular';
import 'angular-resource';
import 'angular-filter';

import hostessPageComponent from './hostess-page.component';
import hostessCheckinComponent from './hostess-checkin.component';
import hostessSeatingComponent from './hostess-seating.component';

import hostessAPIService from './hostess-api.service';

const HostessModule = angular.module('hostess', [
	'ngResource',
	'angular.filter',

])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	})
	.factory('hostessAPIService', hostessAPIService)
	.component('hostessPage', hostessPageComponent)
	.component('hostessCheckin', hostessCheckinComponent)
	.component('hostessSeating', hostessSeatingComponent);

export default HostessModule;