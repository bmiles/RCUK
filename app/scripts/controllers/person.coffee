'use strict'

angular.module('rcukApp')
  .controller 'PersonCtrl', ($scope) ->
    $scope.things = $routeparams
    
    #some code that grabs all project titles and abstracts from the person object. Using person.id from the route params.
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]
