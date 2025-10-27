class SetValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, name_ten, status_ddt=77):
        self.name_ten = name_ten
        self.status_ddt = status_ddt
        self.created_at = "2025-10-27 09:31:02"
    
    def get_info(self):
        return {
            "name_ten": self.name_ten,
            "status_ddt": self.status_ddt,
            "created_at": self.created_at
        }
    
    def update_name_ten(self, new_value):
        old_value = self.name_ten
        self.name_ten = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetValue("sample_data", 24)
print(obj.get_info())
