service_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 4, "maxLength": 40},
        "short_description": {"type": "string", "minLength": 20, "maxLength": 400},
        "long_description": {"type": "string", "maxLength": 9000},
        "rubric_id": {"type": "number"},
        "payment_interval_id": {"type": "number"},
        "price": {"type": "number"},
      },
    "required": []
}