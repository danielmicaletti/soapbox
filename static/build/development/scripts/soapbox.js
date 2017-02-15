(function(){
	'use strict';
	angular
		.module('soapbox', [
			'ngAnimate',
			'ngSanitize',
			'ngCookies',
			'ngFileUpload',
			'ui.router',
			'ui.bootstrap',
			'soapbox.config',
			'soapbox.routes',
			'main',
			'users'
		]);

	angular
		.module('soapbox.config', ['ui.router']);

	angular
		.module('soapbox.routes', ['ui.router.router'])

	angular
		.module('soapbox')
		.run(runCSRF);

	runCSRF.$inject = ['$http'];

	function runCSRF($http){
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';
	};

    angular
        .module('soapbox')
        .run(runIsAuthAcct);

    runIsAuthAcct.$inject = ['$rootScope', '$state', 'Main'];

    function runIsAuthAcct($rootScope, $state, Main) {
        $rootScope.$on('$stateChangeStart', function(event, toState, toParams) {
            var requireLogin = toState.data.requireLogin;
            var auth = Main.isAuthAcct();

            if(requireLogin && !auth){
                event.preventDefault();
                $state.go('login');
                return $rootScope;
            }
        });
    }

})();