'use strict'

describe 'Controller: ResultCtrl', () ->

  # load the controller's module
  beforeEach module 'rcukApp'

  ResultCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    ResultCtrl = $controller 'ResultCtrl', {
      $scope: scope
    }

  it 'should attach a list of awesomeThings to the scope', () ->
    expect(scope.awesomeThings.length).toBe 3
