class SetItem:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, array_ezc, value_rem=1):
        self.array_ezc = array_ezc
        self.value_rem = value_rem
        self.created_at = "2026-02-11 11:00:45"
    
    def get_info(self):
        return {
            "array_ezc": self.array_ezc,
            "value_rem": self.value_rem,
            "created_at": self.created_at
        }
    
    def update_array_ezc(self, new_value):
        old_value = self.array_ezc
        self.array_ezc = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetItem("sample_data", 43)
print(obj.get_info())
