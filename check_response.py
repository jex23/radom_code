class SetData:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, result_jsy, node_zhx=1):
        self.result_jsy = result_jsy
        self.node_zhx = node_zhx
        self.created_at = "2025-09-19 11:50:06"
    
    def get_info(self):
        return {
            "result_jsy": self.result_jsy,
            "node_zhx": self.node_zhx,
            "created_at": self.created_at
        }
    
    def update_result_jsy(self, new_value):
        old_value = self.result_jsy
        self.result_jsy = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = SetData("sample_data", 46)
print(obj.get_info())
