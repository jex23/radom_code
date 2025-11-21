class CheckRequest:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, item_gkk, args_hpv=31):
        self.item_gkk = item_gkk
        self.args_hpv = args_hpv
        self.created_at = "2025-11-21 13:29:06"
    
    def get_info(self):
        return {
            "item_gkk": self.item_gkk,
            "args_hpv": self.args_hpv,
            "created_at": self.created_at
        }
    
    def update_item_gkk(self, new_value):
        old_value = self.item_gkk
        self.item_gkk = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CheckRequest("sample_data", 15)
print(obj.get_info())
