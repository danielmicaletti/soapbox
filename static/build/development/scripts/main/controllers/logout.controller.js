(function () {
    'use strict';

    angular
        .module('main.controllers')
        .controller('LogoutController', LogoutController);

    LogoutController.$inject = ['$state', 'Main'];

    function LogoutController($state, Main){
        var vm = this;

        activate();

        function activate(){
            if(Main.isAuthAcct()){
                Main.logout();
            } else {
                $state.go('login');
            }

        }
    }
})();
