vacancy_offer_schema = {
    "type": "object",
    "properties": {
        "description": {"type": "string", "minLength": 50, "maxLength": 2500},
        "price": {"type": "number", "minimum": 500, "maximum": 500000},
        "vacancy_id": {"type": "number"},
        "payment_interval_id": {"type": "number"},
      },
    "required": []
}
