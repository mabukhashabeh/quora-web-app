import uuid

STRING_LENGTH = 6


def generate_random_string(length=STRING_LENGTH):
    return uuid.uuid4().hex[:length].lower()
