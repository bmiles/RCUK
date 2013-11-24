'use strict'

angular.module('rcukApp')
  .factory 'Search', ["$http", ($http) ->
    query: (terms) ->
      $http.get("http://localhost:5000/search/#{terms}")
      .success (res) ->
        return res
  ]
