def generate_id(data):
    if not data:
        return 1
    return max(d["student_id"] for d in data) + 1