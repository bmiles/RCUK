'use strict'

angular.module('rcukApp')
  .controller 'MainCtrl', ($scope, personStorage, $http, $location) ->
    
    $scope.showResults = (searchTerm) ->
      console.log(searchTerm)
      $location.path("/result/"+ searchTerm)
      
    $scope.popularSearches = [
      'Cryopreservation'
      'Nanoparticles'
      'Graphene'
      'Mechatronics'
      'Superhydrophobic Surfaces'
      'Statins'
      'Gene therapy'
    ]    
