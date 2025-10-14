class CreateItem:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, id_cfg, args_ukj=52):
        self.id_cfg = id_cfg
        self.args_ukj = args_ukj
        self.created_at = "2025-10-14 18:30:32"
    
    def get_info(self):
        return {
            "id_cfg": self.id_cfg,
            "args_ukj": self.args_ukj,
            "created_at": self.created_at
        }
    
    def update_id_cfg(self, new_value):
        old_value = self.id_cfg
        self.id_cfg = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateItem("sample_data", 33)
print(obj.get_info())
