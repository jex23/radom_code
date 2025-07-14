class DeleteConfig:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, value_hyi, array_gjx=72):
        self.value_hyi = value_hyi
        self.array_gjx = array_gjx
        self.created_at = "2025-07-14 20:07:11"
    
    def get_info(self):
        return {
            "value_hyi": self.value_hyi,
            "array_gjx": self.array_gjx,
            "created_at": self.created_at
        }
    
    def update_value_hyi(self, new_value):
        old_value = self.value_hyi
        self.value_hyi = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = DeleteConfig("sample_data", 43)
print(obj.get_info())
