'use strict'

angular.module('rcukApp')
  .controller 'ResultCtrl', ["$scope", "Search", "$routeParams", "$location", "promiseTracker", "$rootScope", ($scope, Search, $routeParams, $location, promiseTracker, $rootScope) ->
    
    $rootScope.tracker = promiseTracker("resultTracker",
      minDuration: 1000 #add this so we can actually see it come up
    )
    
    Search.query $routeParams.searchTerm, $scope

    $scope.showPerson = (person) ->
      console.log(person._id.$oid)
      $location.path("/person/"+ person._id.$oid)
  ]
