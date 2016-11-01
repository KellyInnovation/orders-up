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
    .config(($stateProvider) => {

        $stateProvider.state('index', {
            url: '/',
            // resolve: {
            //     parties(
            //         partyAPIService) {
            //         return partyAPIService.getAllParties();
            //     },
            // },
            component: 'partyPage',
        });
    });

export default AppModule;
