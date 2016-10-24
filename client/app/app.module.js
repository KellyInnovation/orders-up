import angular from 'angular';

import GuestModule from '../guest/guest.module';
import HostessModule from '../hostess/hostess.module';

import appComponent from './app.component';

const AppModule = angular.module('app', [
	GuestModule.name,
	HostessModule.name,
])
    .component('app', appComponent);

export default AppModule;
