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
        }).state('party', {
            url: '/party',
            component: 'partyPage',    
        }).state('kitchen', {
            url: '/kitchen',
            component: 'kitchenPage',
        // }).state('kitchen-form', {
        //     url: 'kitchen-form',
        //     resolve: {
        //         menu,
        //     }
        //     component: 'kitchenForm'
        }).state('hostess', {
            url: '/hostess',
            component: 'hostessPage',
        });
    });

export default AppModule;
