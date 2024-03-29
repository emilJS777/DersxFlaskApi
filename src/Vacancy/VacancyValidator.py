vacancy_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 5, "maxLength": 50},
        "short_description": {"type": "string", "minLength": 20, "maxLength": 600},
        "long_description": {"type": "string", "minLength": 20, "maxLength": 4000},
        "rubric_id": {"type": "number"},
        "payment_interval_id": {"type": "number"},
        "price": {"type": "number", "minimum": 0, "maximum": 1000000},
      },
    "required": []
}