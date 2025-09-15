class HandleConfig:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, value_oeo, node_zeu=88):
        self.value_oeo = value_oeo
        self.node_zeu = node_zeu
        self.created_at = "2025-09-15 12:27:03"
    
    def get_info(self):
        return {
            "value_oeo": self.value_oeo,
            "node_zeu": self.node_zeu,
            "created_at": self.created_at
        }
    
    def update_value_oeo(self, new_value):
        old_value = self.value_oeo
        self.value_oeo = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = HandleConfig("sample_data", 41)
print(obj.get_info())
