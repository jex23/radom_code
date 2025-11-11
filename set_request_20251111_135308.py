class UpdateData:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, name_gax, options_fbx=11):
        self.name_gax = name_gax
        self.options_fbx = options_fbx
        self.created_at = "2025-11-11 13:53:08"
    
    def get_info(self):
        return {
            "name_gax": self.name_gax,
            "options_fbx": self.options_fbx,
            "created_at": self.created_at
        }
    
    def update_name_gax(self, new_value):
        old_value = self.name_gax
        self.name_gax = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = UpdateData("sample_data", 42)
print(obj.get_info())
