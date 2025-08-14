class HandleResponse:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, count_tjr, string_rsw=64):
        self.count_tjr = count_tjr
        self.string_rsw = string_rsw
        self.created_at = "2025-08-14 14:45:07"
    
    def get_info(self):
        return {
            "count_tjr": self.count_tjr,
            "string_rsw": self.string_rsw,
            "created_at": self.created_at
        }
    
    def update_count_tjr(self, new_value):
        old_value = self.count_tjr
        self.count_tjr = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = HandleResponse("sample_data", 27)
print(obj.get_info())
