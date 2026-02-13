class SetRequest:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, type_bww, name_lpv=58):
        self.type_bww = type_bww
        self.name_lpv = name_lpv
        self.created_at = "2026-02-13 14:41:07"
    
    def get_info(self):
        return {
            "type_bww": self.type_bww,
            "name_lpv": self.name_lpv,
            "created_at": self.created_at
        }
    
    def update_type_bww(self, new_value):
        old_value = self.type_bww
        self.type_bww = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetRequest("sample_data", 33)
print(obj.get_info())
