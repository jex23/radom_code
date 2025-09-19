class SetValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, response_bxm, count_hbx=55):
        self.response_bxm = response_bxm
        self.count_hbx = count_hbx
        self.created_at = "2025-09-19 17:14:12"
    
    def get_info(self):
        return {
            "response_bxm": self.response_bxm,
            "count_hbx": self.count_hbx,
            "created_at": self.created_at
        }
    
    def update_response_bxm(self, new_value):
        old_value = self.response_bxm
        self.response_bxm = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetValue("sample_data", 16)
print(obj.get_info())
