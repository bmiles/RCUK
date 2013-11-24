'use strict'

angular.module('rcukApp')
  .controller 'PersonCtrl', ["$scope", "Person", "$routeParams", ($scope, Person, $routeParams) ->
    Person.get $routeParams.id, $scope
  ]
