link_schema = {
    "href": {
        "type": "string"
    },
    "rel": {
        "type": "string",
        "allowed": ["PI_PER", "COI_PER", "PM_PER", "FELLOW_PER", "EMPLOYEE",
                    "EMPLOYED", "LEAD_ORG", "COLLAB_ORG", "FELLOW_ORG",
                    "COFUND_ORG", "PP_ORG", "FUNDER", "PROJECT"]
    },
}

organisation_schema = {
    "id": {
        "type": "string"
    },
    "href": {
        "type": "string"
    },
    # handled automatically by Eve
    # "created": {
    #     "type": "datetime"
    # },
    # "updated": {
    #     "type": "datetime",
    #     "nullable": True,
    # },
    "name": {
        "type": "string"
    },
    "regNumber": {
        "type": "string",
        "nullable": True,
    },
    "website": {
        "type": "string",
        "nullable": True,
    },
}

person_schema = {
    "id": {
        "type": "string"
    },
    "href": {
        "type": "string"
    },
    # handled automatically by Eve
    # "created": {
    #     "type": "datetime"
    # },
    # "updated": {
    #     "type": "datetime",
    #     "nullable": True,
    # },
    "firstName": {
        "type": "string"
    },
    "otherNames": {
        "type": "string",
        "nullable": True,
    },
    "surname": {
        "type": "string"
    },
    "email": {
        "type": "string",
        "nullable": True,
    },
}

project_schema = {
    "id": {
        "type": "string"
    },
    "href": {
        "type": "string"
    },
    # handled automatically by Eve
    # "created": {
    #     "type": "datetime"
    # },
    # "updated": {
    #     "type": "datetime",
    #     "nullable": True,
    # },
    "title": {
        "type": "string"
    },
    "abstractText": {
        "type": "string",
        "nullable": True,
    },
}
