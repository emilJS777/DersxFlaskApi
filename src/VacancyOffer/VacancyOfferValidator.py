vacancy_offer_schema = {
    "type": "object",
    "properties": {
        "description": {"type": "string", "minLength": 0, "maxLength": 2500},
        "price": {"type": "number", "minimum": 0, "maximum": 1000000},
        "vacancy_id": {"type": "number"},
        "payment_interval_id": {"type": "number"},
      },
    "required": []
}
