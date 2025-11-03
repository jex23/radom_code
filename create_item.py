class ValidateValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, response_uju, options_dea=5):
        self.response_uju = response_uju
        self.options_dea = options_dea
        self.created_at = "2025-11-03 18:12:10"
    
    def get_info(self):
        return {
            "response_uju": self.response_uju,
            "options_dea": self.options_dea,
            "created_at": self.created_at
        }
    
    def update_response_uju(self, new_value):
        old_value = self.response_uju
        self.response_uju = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ValidateValue("sample_data", 17)
print(obj.get_info())
