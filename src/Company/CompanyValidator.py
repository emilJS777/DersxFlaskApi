company_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 40},
        "short_description": {"type": "string", "minLength": 15, "maxLength": 300},
        "long_description": {"type": "string", "maxLength": 9000},
      },
    "required": []
}