vacancy_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 5, "maxLength": 50},
        "short_description": {"type": "string", "minLength": 50, "maxLength": 600},
        "long_description": {"type": "string", "minLength": 50, "maxLength": 4000},
        "rubric_id": {"type": "number"},
        "payment_interval_id": {"type": "number"},
        "price": {"type": "number"}
      },
    "required": []
}