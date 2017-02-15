(function () {
    'use strict';

    angular
        .module('main.controllers')
        .controller('AppController', AppController);

    AppController.$inject = ['$scope', '$sce', '$state', 'Main', 'Users'];

    function AppController($scope, $sce, $state, Main, Users){
        var vm = this;

        activate();

        function activate(){
            console.log('APP');
            if(Main.isAuthAcct()){
                vm.authAcct = Main.getAuthAcct();

                Users.getUser(vm.authAcct.id).then(function(response){
                    vm.currentUser = response;
                }).catch(function(errMsg){
                    Main.logout();
                });

            } else {
                console.log("Could not get account");
                $state.go('login');
            }
        }

        // $scope.$on("update_user_info", function(event, message){
        //     if(vm.authAcct.id == message.id){
        //         vm.currentUser = message;
        //     }
        // });

        var mediaPath = media_path('');
        var staticPath = static_path('');

        $scope.path = { 
            static_files: $sce.trustAsResourceUrl(staticPath),
            media: $sce.trustAsResourceUrl(mediaPath),
        };

    }
})();
