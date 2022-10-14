user_contact_schema = {
    "type": "object",
    "properties": {
        "type": {"type": "string", "maxLength": 40},
        "information": {"type": "string", "maxLength": 120}
    },
    "required": ["type", "information"]
}
