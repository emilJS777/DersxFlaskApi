user_about_schema = {
    "type": "object",
    "properties": {
        "description": {"type": "string", "minLength": 20, "maxLength": 6000}
      },
    "required": ["description"]
}
