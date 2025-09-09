class HandleItem:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, list_fre, array_zii=24):
        self.list_fre = list_fre
        self.array_zii = array_zii
        self.created_at = "2025-09-09 10:39:04"
    
    def get_info(self):
        return {
            "list_fre": self.list_fre,
            "array_zii": self.array_zii,
            "created_at": self.created_at
        }
    
    def update_list_fre(self, new_value):
        old_value = self.list_fre
        self.list_fre = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = HandleItem("sample_data", 50)
print(obj.get_info())
