import angular from 'angular';
import uiRouter from 'angular-ui-router';

import GuestModule from '../guest/guest.module';
import HostessModule from '../hostess/hostess.module';
import KitchenModule from '../kitchen/kitchen.module';
import PartyModule from '../party/party.module'

import appComponent from './app.component';

const AppModule = angular.module('app', [
	uiRouter,
	GuestModule.name,
	HostessModule.name,
	KitchenModule.name,
	PartyModule.name,
])
    .component('app', appComponent)
    .config(function($stateProvider) {
    	var partyState = {
    		name: 'party',
    		url: 'party-page.html',
    	}
    $stateProvider.state(partyState);
    });

export default AppModule;
