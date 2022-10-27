forum_discussion_schema = {
    "type": "object",
    "properties": {
        "description": {"type": "string", "minLength": 1, "maxLength": 4000},
        "forum_id": {"type": "number"}
      },
    "required": []
}
