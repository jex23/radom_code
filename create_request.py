class HandleItem:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, node_dnr, key_xui=7):
        self.node_dnr = node_dnr
        self.key_xui = key_xui
        self.created_at = "2025-09-16 21:18:18"
    
    def get_info(self):
        return {
            "node_dnr": self.node_dnr,
            "key_xui": self.key_xui,
            "created_at": self.created_at
        }
    
    def update_node_dnr(self, new_value):
        old_value = self.node_dnr
        self.node_dnr = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = HandleItem("sample_data", 21)
print(obj.get_info())
