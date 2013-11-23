'use strict'

describe 'Directive: myNavbar', () ->

  # load the directive's module
  beforeEach module 'rcukApp'

  scope = {}

  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()

  it 'should make hidden element visible', inject ($compile) ->
    element = angular.element '<my-navbar></my-navbar>'
    element = $compile(element) scope
    expect(element.text()).toBe 'this is the myNavbar directive'
