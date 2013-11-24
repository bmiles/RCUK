'use strict'

angular.module('rcukApp')
  .controller 'PersonCtrl', ($scope) ->
    console.log($routeParams)
    $scope.things = $routeParams
    
    #some code that grabs all project titles and abstracts from the person object. Using person.id from the route params.
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]
