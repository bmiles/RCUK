'use strict'

angular.module('rcukApp')
  .controller 'MainCtrl', ($scope, personStorage, $http) ->
    $scope.persons = personStorage.getPersons()
    
    getTitle = (projectLink) ->
      console.log(projectLink)
      
      $http.get(projectLink).success
      
    $scope.projectTitle = getTitle($scope.persons[0].links.link[0].href)
    
    #search function
    topicSearch = (searchTerm) ->
      console.log(searchTerm)
       
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]
