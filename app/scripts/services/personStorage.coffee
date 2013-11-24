'use strict'

angular.module('rcukApp')
  .factory('Search', ["$http", ($http) ->
    query: (terms, scope) ->
      $http.get("/search/#{terms}")
      .success (res) ->
        scope.persons = res
  ])
  .factory('Person', ["$http", ($http) ->
    get: (id, scope) ->
      $http.get("/api/persons/#{id}")
      .success (res) ->
        console.log "Person #{id}", res
        scope.person = res
  ])
