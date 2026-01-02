class CreateValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, data_ejg, index_swm=1):
        self.data_ejg = data_ejg
        self.index_swm = index_swm
        self.created_at = "2026-01-02 11:47:07"
    
    def get_info(self):
        return {
            "data_ejg": self.data_ejg,
            "index_swm": self.index_swm,
            "created_at": self.created_at
        }
    
    def update_data_ejg(self, new_value):
        old_value = self.data_ejg
        self.data_ejg = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateValue("sample_data", 30)
print(obj.get_info())
