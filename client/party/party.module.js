import angular from 'angular';
import angularResource from 'angular-resource';


import partyPageComponent from './party-page.component';

import partyAPIService from './party-api.service';

const PartyModule = angular.module(
	'parties', [
	angularResource,

])
	.factory('partyAPIService', partyAPIService) 
	.component('partyPage', partyPageComponent);

export default PartyModule;