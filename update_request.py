class DeleteValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, config_yem, list_rnm=45):
        self.config_yem = config_yem
        self.list_rnm = list_rnm
        self.created_at = "2025-08-07 13:40:03"
    
    def get_info(self):
        return {
            "config_yem": self.config_yem,
            "list_rnm": self.list_rnm,
            "created_at": self.created_at
        }
    
    def update_config_yem(self, new_value):
        old_value = self.config_yem
        self.config_yem = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = DeleteValue("sample_data", 46)
print(obj.get_info())
