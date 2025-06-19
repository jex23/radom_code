class ValidateValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, list_pco, data_flx=85):
        self.list_pco = list_pco
        self.data_flx = data_flx
        self.created_at = "2025-06-19 13:36:05"
    
    def get_info(self):
        return {
            "list_pco": self.list_pco,
            "data_flx": self.data_flx,
            "created_at": self.created_at
        }
    
    def update_list_pco(self, new_value):
        old_value = self.list_pco
        self.list_pco = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ValidateValue("sample_data", 45)
print(obj.get_info())
