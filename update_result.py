class CheckValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, array_ipx, data_zgu=70):
        self.array_ipx = array_ipx
        self.data_zgu = data_zgu
        self.created_at = "2025-06-13 15:17:07"
    
    def get_info(self):
        return {
            "array_ipx": self.array_ipx,
            "data_zgu": self.data_zgu,
            "created_at": self.created_at
        }
    
    def update_array_ipx(self, new_value):
        old_value = self.array_ipx
        self.array_ipx = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CheckValue("sample_data", 48)
print(obj.get_info())
