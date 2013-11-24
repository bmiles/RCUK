'use strict'

angular.module('rcukApp')
  .factory('Search', ["$http", ($http) ->
    query: (terms, scope) ->
      $http.get("/search/#{terms}")
      .success (res) ->
        scope.persons = res
  ])
  .factory('Person', ["$http", "Project", ($http, Project) ->
    get: (id, scope) ->
      $http.get("/api/persons/#{id}")
      .success (person) ->
        if person.PI_PER?
          person.pi = []
          for pid in person.PI_PER
            Project.get pid, person.pi
        if person.COI_PER?
          person.coi = []
          for pid in person.COI_PER
            Project.get pid, person.coi
        console.log "Person #{id}", person
        scope.person = person
  ])
  .factory('Project', ["$http", ($http) ->
    get: (id, scope) ->
      $http.get("/api/projects/#{id}")
      .success (res) ->
        console.log "Project #{id}", res
        scope.push res
  ])
