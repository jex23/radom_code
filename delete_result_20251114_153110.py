class CreateRequest:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, node_ihb, data_gkx=76):
        self.node_ihb = node_ihb
        self.data_gkx = data_gkx
        self.created_at = "2025-11-14 15:31:10"
    
    def get_info(self):
        return {
            "node_ihb": self.node_ihb,
            "data_gkx": self.data_gkx,
            "created_at": self.created_at
        }
    
    def update_node_ihb(self, new_value):
        old_value = self.node_ihb
        self.node_ihb = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CreateRequest("sample_data", 34)
print(obj.get_info())
