class HandleResponse:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, result_uou, response_kis=27):
        self.result_uou = result_uou
        self.response_kis = response_kis
        self.created_at = "2025-12-07 00:56:08"
    
    def get_info(self):
        return {
            "result_uou": self.result_uou,
            "response_kis": self.response_kis,
            "created_at": self.created_at
        }
    
    def update_result_uou(self, new_value):
        old_value = self.result_uou
        self.result_uou = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = HandleResponse("sample_data", 29)
print(obj.get_info())
