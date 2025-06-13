class SetItem:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, string_mwg, name_erb=51):
        self.string_mwg = string_mwg
        self.name_erb = name_erb
        self.created_at = "2025-06-13 12:47:04"
    
    def get_info(self):
        return {
            "string_mwg": self.string_mwg,
            "name_erb": self.name_erb,
            "created_at": self.created_at
        }
    
    def update_string_mwg(self, new_value):
        old_value = self.string_mwg
        self.string_mwg = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetItem("sample_data", 42)
print(obj.get_info())
