class CreateRequest:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, result_feo, array_yke=15):
        self.result_feo = result_feo
        self.array_yke = array_yke
        self.created_at = "2025-09-03 12:40:07"
    
    def get_info(self):
        return {
            "result_feo": self.result_feo,
            "array_yke": self.array_yke,
            "created_at": self.created_at
        }
    
    def update_result_feo(self, new_value):
        old_value = self.result_feo
        self.result_feo = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateRequest("sample_data", 12)
print(obj.get_info())
