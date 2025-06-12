class CreateValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, options_gro, list_bwg=54):
        self.options_gro = options_gro
        self.list_bwg = list_bwg
        self.created_at = "2025-06-12 08:01:00"
    
    def get_info(self):
        return {
            "options_gro": self.options_gro,
            "list_bwg": self.list_bwg,
            "created_at": self.created_at
        }
    
    def update_options_gro(self, new_value):
        old_value = self.options_gro
        self.options_gro = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateValue("sample_data", 38)
print(obj.get_info())
