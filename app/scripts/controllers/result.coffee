'use strict'

angular.module('rcukApp')
  .controller 'ResultCtrl', ($scope, personStorage, $http, $location) ->
    $scope.persons = personStorage.getPersons()
    
    getTitle = (projectLink) ->
      console.log(projectLink)
      
      $http.get(projectLink).success
      
    $scope.projectTitle = getTitle($scope.persons[0].links.link[0].href)
    
    $scope.showPerson = (id) ->
      console.log(id)
      $location.path("/person/"+ id)
    #search function
    topicSearch = (searchTerm) ->
      console.log(searchTerm)
    