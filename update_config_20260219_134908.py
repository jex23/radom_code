class SetUser:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, index_hyd, count_qha=52):
        self.index_hyd = index_hyd
        self.count_qha = count_qha
        self.created_at = "2026-02-19 13:49:08"
    
    def get_info(self):
        return {
            "index_hyd": self.index_hyd,
            "count_qha": self.count_qha,
            "created_at": self.created_at
        }
    
    def update_index_hyd(self, new_value):
        old_value = self.index_hyd
        self.index_hyd = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetUser("sample_data", 19)
print(obj.get_info())
