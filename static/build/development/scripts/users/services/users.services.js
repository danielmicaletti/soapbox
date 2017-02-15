(function () {
    'use strict';

    angular
        .module('users.services')
        .factory('Users', Users);

    Users.$inject = ['$http', '$q', '$state', '$cookies'];

    function Users($http, $q, $state, $cookies) {
        var vm = this;

        var Users = {
            getAll: getAll,
            getUser: getUser,
        };

        return Users;

        function generalCallbackSuccess(response){
            return response.data;
        }

        function generalCallbackError(response){
            return $q.reject('Errors '+response.status+'');
        }

        function getAll(){
            var acct = $cookies.getObject('authAcct');
            // $http.defaults.headers.common['Authorization'] = 'JWT ' + acct.token;
            return $http.get('api/v1/users/', {
                   'Authorization': 'JWT ' + acct.token
                })
                .then(generalCallbackSuccess)
                .catch(generalCallbackError);
        }

        function getUser(userId){
            var acct = $cookies.getObject('authAcct');
            // $http.defaults.headers.common['Authorization'] = 'JWT ' + acct.token;
            return $http.get('api/v1/users/'+userId+'/', {
                   'Authorization': 'JWT ' + acct.token
                })
                .then(generalCallbackSuccess)
                .catch(generalCallbackError);
        }

    }
})();
