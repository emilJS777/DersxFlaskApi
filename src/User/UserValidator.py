user_create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "password": {"type": "string", "minLength": 6, "maxLength": 24},
        "first_name": {"type": "string", "minLength": 3, "maxLength": 60},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 60},
        "date_birth": {"type": "string"},
        "region": {"type": "string", "minLength": 1, "maxLength": 60},
        "email_address": {"type": "string", "minLength": 6, "maxLength": 120},
        "role_id": {"type": "number"},
        "gender_id": {"type": "number"}
      },
    "required": ["name", "password", "first_name", "last_name"]
}

user_update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "first_name": {"type": "string", "minLength": 3, "maxLength": 60},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 60},
        "date_birth": {"type": "string"},
        "region": {"type": "string", "maxLength": 60},
        "email_address": {"type": "string", "maxLength": 120},
        "role_id": {"type": "number"},
        "gender_id": {"type": "number"}
      },
    "required": []
}