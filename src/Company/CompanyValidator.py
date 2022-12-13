company_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 60},
        "short_description": {"type": "string", "minLength": 20, "maxLength": 400},
        "long_description": {"type": "string", "maxLength": 9000},
      },
    "required": []
}