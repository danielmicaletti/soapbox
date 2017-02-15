(function(){
	'use strict';

	angular
		.module('main.controllers')
		.controller('AuthenticationController', AuthenticationController);

	AuthenticationController.$inject = ['$scope', '$sce', '$state', 'Main', 'Users'];

	function AuthenticationController($scope, $sce, $state, Main, Users){
		var vm = this;
		
		activate();

		function activate(){
            if(Main.isAuthAcct()){
                vm.authUser = Main.getAuthAcct();
                $state.go('app.dashboard', {'userId': vm.authUser.id});
            }
		}
		
        vm.goToSignup = function(){

            $('html, body').animate({
                scrollTop: $('#signup').offset().top
            }, 300);
        }

        vm.login = function(username, password){

            Main.login(username, password)
                .then(loginSuccess)
                .catch(loginError);
        }

        function loginSuccess(response){
            $state.go('app.dashboard', {'userId': response.id});
        }

        function loginError(errMsg){
            console.log(errMsg);
            vm.loginError = errMsg.data.message;
        }

        vm.register = function(newUser){
            if(newUser.password === newUser.confirm_password){
                Main.register(newUser)
                    .then(registerSuccess)
                    .catch(registerError);
            } else {
                vm.registerError = "Passwords must match!"
            }
        }

        function registerSuccess(response){
            $scope.isCollapsed = false;
            $scope.registerForm.$setPristine();
            vm.newUser = {};
            $state.go('login');
        }

        function registerError(errMsg){
            console.log(errMsg);
            if(errMsg.status === 500){
                vm.registerError = "username or email in use"
            } else {
                vm.registerError = errMsg.data.message;
            }
        }

        var mediaPath = media_path('');
        var staticPath = static_path('');

        $scope.path = { 
            static_files: $sce.trustAsResourceUrl(staticPath),
            media: $sce.trustAsResourceUrl(mediaPath),
        };
	}
})();