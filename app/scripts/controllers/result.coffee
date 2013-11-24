'use strict'

angular.module('rcukApp')
  .controller 'ResultCtrl', ["$scope", "Search", "$routeParams", ($scope, Search, $routeParams) ->
    Search.query $routeParams.searchTerm, $scope

    #function that gets project titles from a project api URI
#     $scope.getTitle = (projectLink) ->
#       console.log(projectLink)
#       $http.get(projectLink).success
#
#     $scope.projectTitle = getTitle($scope.persons[0].links.link[0].href)

    #topic search function, finds persons based on research topic
#     $scope.topicSearch = (searchTerm) ->
#       searchTermArr = searchTerm.toLowerCase().split(" ")
#       console.log(searchTermArr)
#       $http.get 'http://research-connect.herokuapp.com/api/people',
#         params:
#           where: searchTermArray
#       .success () ->
#           console.log("success")
#           $scope.persons = response.persons

    #Person linking
    $scope.showPerson = (id) ->
      console.log(id)
      $location.path("/person/"+ id)
  ]
