class DeleteData:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, list_thz, list_flo=34):
        self.list_thz = list_thz
        self.list_flo = list_flo
        self.created_at = "2025-12-25 13:32:23"
    
    def get_info(self):
        return {
            "list_thz": self.list_thz,
            "list_flo": self.list_flo,
            "created_at": self.created_at
        }
    
    def update_list_thz(self, new_value):
        old_value = self.list_thz
        self.list_thz = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = DeleteData("sample_data", 50)
print(obj.get_info())
