(function () {
    'use strict';

    angular
        .module('soapbox.routes')
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    function config($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise(function ($injector) {
            var $state = $injector.get('$state');
            $state.go('app.dashboard');
        });

        $stateProvider
            .state('app', {
                abstract: true,
                url: '/app',
                controller: 'AppController',
                controllerAs: 'vm',     
                templateUrl: static_path('views/main/app.html'),
                data: {
                    requireLogin: true
                },
            })
            .state('app.dashboard', {
                url: '/dashboard/:userId',
                controller: 'DashBoardController',
                controllerAs: 'vm',     
                templateUrl: static_path('views/main/dashboard.html'),
                data: {
                    requireLogin: true
                },
            })
            .state('login', {
                url: '/login',
                controller: 'AuthenticationController',
                controllerAs: 'vm',     
                templateUrl: static_path('views/main/login.html'),
                data: {
                    requireLogin: false
                },
            })
            .state('logout', {
                url: '/logout',
                controller: 'LogoutController',
                controllerAs: 'vm',
                data: {
                    requireLogin: true
                },
            });
    }
})();

