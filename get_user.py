class ValidateUser:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, index_akh, index_swz=40):
        self.index_akh = index_akh
        self.index_swz = index_swz
        self.created_at = "2025-07-30 09:36:17"
    
    def get_info(self):
        return {
            "index_akh": self.index_akh,
            "index_swz": self.index_swz,
            "created_at": self.created_at
        }
    
    def update_index_akh(self, new_value):
        old_value = self.index_akh
        self.index_akh = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ValidateUser("sample_data", 48)
print(obj.get_info())
