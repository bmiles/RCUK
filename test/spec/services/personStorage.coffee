'use strict'

describe 'Service: Personstorage', () ->

  # load the service's module
  beforeEach module 'rcukApp'

  # instantiate service
  Personstorage = {}
  beforeEach inject (_Personstorage_) ->
    Personstorage = _Personstorage_

  it 'should do something', () ->
    expect(!!Personstorage).toBe true
