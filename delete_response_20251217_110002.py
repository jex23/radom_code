class CreateValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, name_wuh, name_odr=10):
        self.name_wuh = name_wuh
        self.name_odr = name_odr
        self.created_at = "2025-12-17 11:00:02"
    
    def get_info(self):
        return {
            "name_wuh": self.name_wuh,
            "name_odr": self.name_odr,
            "created_at": self.created_at
        }
    
    def update_name_wuh(self, new_value):
        old_value = self.name_wuh
        self.name_wuh = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateValue("sample_data", 41)
print(obj.get_info())
