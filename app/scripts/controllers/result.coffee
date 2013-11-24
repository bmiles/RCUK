'use strict'

angular.module('rcukApp')
  .controller 'ResultCtrl', ["$scope", "Search", "$routeParams", "$location", ($scope, Search, $routeParams, $location) ->
    Search.query $routeParams.searchTerm, $scope

    $scope.showPerson = (person) ->
      console.log(person._id.$oid)
      $location.path("/person/"+ person._id.$oid)
  ]
