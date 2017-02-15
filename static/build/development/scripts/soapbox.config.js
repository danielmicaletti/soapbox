(function () {
    'use strict';

    angular
        .module('soapbox.config')
        .config(config);

    config.$inject = ['$locationProvider', '$urlMatcherFactoryProvider', '$httpProvider'];

    function config($locationProvider, $urlMatcherFactoryProvider, $httpProvider) {
        // $locationProvider.html5Mode({enabled: true, requireBase: false});
        // $locationProvider.hashPrefix('!');
        $httpProvider.interceptors.push('tokenInterceptor');
		$urlMatcherFactoryProvider.caseInsensitive(true);
		$urlMatcherFactoryProvider.strictMode(false); 
    }
})();