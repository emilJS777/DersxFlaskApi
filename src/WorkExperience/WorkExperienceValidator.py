work_experience_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 80},
        "link": {"type": "string", "maxLength": 420},
        "skills": {"type": "string", "maxLength": 120},
        "description": {"type": "string"},
        "date_start": {"type": "string"},
        "date_end": {"type": "string"},
      },
    "required": []
}
