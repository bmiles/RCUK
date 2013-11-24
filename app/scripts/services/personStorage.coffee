'use strict'

angular.module('rcukApp')
  .factory 'Search', ["$http", ($http) ->
    query: (terms, scope) ->
      $http.get("/search/#{terms}")
      .success (res) ->
        scope.persons = res
  ]
