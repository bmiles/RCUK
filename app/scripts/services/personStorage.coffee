'use strict'

angular.module('rcukApp')
  .factory('Search', ["$http", ($http) ->
    query: (terms, scope) ->
      $http.get("/search/#{terms}")
      .success (res) ->
        scope.persons = res
  ])
  .factory('Person', ["$http", "Organisation", "Project", ($http, Organisation, Project) ->
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
        if person.EMPLOYED?
          person.employer = []
          for oid in person.EMPLOYED
            Organisation.get oid, person.employer
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
  .factory('Organisation', ["$http", ($http) ->
    get: (id, scope) ->
      $http.get("/api/organisations/#{id}")
      .success (res) ->
        console.log "Organisation #{id}", res
        scope.push res
  ])
