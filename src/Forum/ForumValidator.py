forum_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 6, "maxLength": 80},
        "topic": {"type": "string", "minLength": 16, "maxLength": 480},
        "rubric_id": {"type": "number"}
      },
    "required": []
}