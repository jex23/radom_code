class DeleteRequest:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, node_ozz, name_kza=44):
        self.node_ozz = node_ozz
        self.name_kza = name_kza
        self.created_at = "2026-02-24 16:10:08"
    
    def get_info(self):
        return {
            "node_ozz": self.node_ozz,
            "name_kza": self.name_kza,
            "created_at": self.created_at
        }
    
    def update_node_ozz(self, new_value):
        old_value = self.node_ozz
        self.node_ozz = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = DeleteRequest("sample_data", 24)
print(obj.get_info())
