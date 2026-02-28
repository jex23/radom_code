class HandleResponse:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, array_mzk, node_ldr=44):
        self.array_mzk = array_mzk
        self.node_ldr = node_ldr
        self.created_at = "2026-02-28 11:46:02"
    
    def get_info(self):
        return {
            "array_mzk": self.array_mzk,
            "node_ldr": self.node_ldr,
            "created_at": self.created_at
        }
    
    def update_array_mzk(self, new_value):
        old_value = self.array_mzk
        self.array_mzk = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = HandleResponse("sample_data", 33)
print(obj.get_info())
