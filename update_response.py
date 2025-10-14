class DeleteValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, name_uov, id_inz=70):
        self.name_uov = name_uov
        self.id_inz = id_inz
        self.created_at = "2025-10-14 12:46:23"
    
    def get_info(self):
        return {
            "name_uov": self.name_uov,
            "id_inz": self.id_inz,
            "created_at": self.created_at
        }
    
    def update_name_uov(self, new_value):
        old_value = self.name_uov
        self.name_uov = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = DeleteValue("sample_data", 26)
print(obj.get_info())
