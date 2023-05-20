create_restore_password_schema = {
    "type": "object",
    "properties": {
        "address": {"type": "string", "maxLength": 120},
      },
    "required": []
}
update_restore_password_schema = {
    "type": "object",
    "properties": {
        "new_password": {"type": "string", "minLength": 6, "maxLength": 24},
      },
    "required": []
}