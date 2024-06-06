class MyString:
    def __init__(self, value=None):
        if value is None:
            value = ''
        # Check if value is not a string, None, or an empty string
        if not isinstance(value, str) or value.strip() == '':
            raise ValueError("The value must be a non-empty string.")
        self.value = value
