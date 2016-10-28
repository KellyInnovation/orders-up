import angular from 'angular';
import uiRouter from 'angular-ui-router';

import GuestModule from '../guest/guest.module';
import HostessModule from '../hostess/hostess.module';
import KitchenModule from '../kitchen/kitchen.module';
import PartyModule from '../party/party.module';

import appComponent from './app.component';

const AppModule = angular.module('app', [
	uiRouter,
	GuestModule.name,
	HostessModule.name,
	KitchenModule.name,
	PartyModule.name,
])
    .component('app', appComponent)
    .config(($stateProvider, $urlRouterProvider) => {
    	$urlRouterProvider.otherwise('/');

    	$stateProvider.state('index', {
    		url: '/',
    		resolve: {
    			party(partyAPIService) {
    				return partyAPIService.getAllparties();
    			},
    		},
    		component: 'partyList',
    	}).state('party', {
    		url: '/party/{partyId}',
    	})
    })
    ;

export default AppModule;
