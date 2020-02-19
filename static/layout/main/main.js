'use strict';

angular.module('myApp.main', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/main', {
    templateUrl: '/static/layout/main/main.html',
    controller: 'MainCtrl'
  });
}])

.controller('MainCtrl', function($scope, $location,$http) {

  $scope.logout = function () {

    $location.path('login')

  };
  get_faces()
 function get_faces() {
    $http({
        method: 'POST',
        url: '/api/faces',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        $scope.param =response.data
    });
};
});