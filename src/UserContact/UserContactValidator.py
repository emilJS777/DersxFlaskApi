user_contact_schema = {
    "type": "object",
    "properties": {
        "type": {"type": "string", "minLength": 3, "maxLength": 40},
        "information": {"type": "string", "minLength": 3, "maxLength": 120}
    },
    "required": ["type", "information"]
}
