import angular from 'angular';
import uiRouter from 'angular-ui-router';
import angularCookies from 'angular-cookies';

import GuestModule from '../guest/guest.module';
import HostessModule from '../hostess/hostess.module';
import KitchenModule from '../kitchen/kitchen.module';
import PartyModule from '../party/party.module'

import appComponent from './app.component';

const AppModule = angular.module('app', [
	uiRouter,
    angularCookies,
	GuestModule.name,
	HostessModule.name,
	KitchenModule.name,
	PartyModule.name,
])
    .component('app', appComponent)
    .config(($stateProvider, $urlRouterProvider, $resourceProvider) => {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $urlRouterProvider.otherwise('/');

        $stateProvider.state('index', {
            url: '/',
        }).state('party', {
            url: '/party/{partyId}',
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
    })
    .run(($http, $cookies) => {
        // Add a header for CSRF token, so that POST does not fail to our API
        $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    });

export default AppModule;
