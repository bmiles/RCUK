'use strict'

angular.module('rcukApp')
  .factory 'personStorage', ($http, $resource) ->
    # Service logic
    persons = `[
    {
    "links": {
        "link": [
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/24D581BA-EFFF-498D-ABAB-67FBD2A6A677",
                "rel": "COI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/6C7D8098-B7C8-4707-B271-FF7EEF4CA118",
                "rel": "COI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/F7B8C5F8-F97D-4891-9C03-67534723E356",
                "rel": "COI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/F810C50A-8408-473A-BDB8-38CB442642E5",
                "rel": "PI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/6745CFB6-1C5B-4628-A395-457951011725",
                "rel": "COI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/DDDFA9CF-4D90-4646-8674-29C1169792D7",
                "rel": "COI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/F7A1C1E8-95FE-486A-91F2-8B66A84A5BB8",
                "rel": "PI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/projects/69465F79-7153-4879-B885-786781468BCC",
                "rel": "PI_PER",
                "start": null,
                "end": null,
                "otherAttributes": {}
            },
            {
                "href": "http://gtr.rcuk.ac.uk:80/gtr/api/organisations/E5AFE7E4-FF5D-4FF1-B50B-E04A6DF7D791",
                "rel": "EMPLOYED",
                "start": null,
                "end": null,
                "otherAttributes": {}
            }
        ]
    },
    "ext": null,
    "id": "2EEB1E0D-57A7-4436-A147-91555125E401",
    "href": "http://gtr.rcuk.ac.uk:80/gtr/api/persons/2EEB1E0D-57A7-4436-A147-91555125E401",
    "created": 1384417886000,
    "updated": null,
    "firstName": "Brian",
    "otherNames": null,
    "surname": "Cox",
    "email": null,
}
]`

    # Public API here
    getPersons: () ->
      persons      
