class ProcessData:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, args_vmd, element_eel=73):
        self.args_vmd = args_vmd
        self.element_eel = element_eel
        self.created_at = "2025-06-24 15:55:24"
    
    def get_info(self):
        return {
            "args_vmd": self.args_vmd,
            "element_eel": self.element_eel,
            "created_at": self.created_at
        }
    
    def update_args_vmd(self, new_value):
        old_value = self.args_vmd
        self.args_vmd = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ProcessData("sample_data", 28)
print(obj.get_info())
