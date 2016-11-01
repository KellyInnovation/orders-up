import template from './app.html';
import AppController from './app.controller';

const appComponent = {
    template,
    bindings: {
    	party: '<',
    },
    controller: AppController,
    controllerAs: 'appCtrl',
};

export default appComponent;
