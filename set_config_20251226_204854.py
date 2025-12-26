class CreateResult:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, key_whz, number_wvx=35):
        self.key_whz = key_whz
        self.number_wvx = number_wvx
        self.created_at = "2025-12-26 20:48:54"
    
    def get_info(self):
        return {
            "key_whz": self.key_whz,
            "number_wvx": self.number_wvx,
            "created_at": self.created_at
        }
    
    def update_key_whz(self, new_value):
        old_value = self.key_whz
        self.key_whz = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateResult("sample_data", 38)
print(obj.get_info())
