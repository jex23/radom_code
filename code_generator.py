import os
import random
import string
import subprocess
import json
from datetime import datetime
# Removed requests import as it's not actually used

class RandomCodeGenerator:
    def __init__(self, repo_path, github_token=None):
        self.repo_path = repo_path
        self.github_token = github_token
        
        # Code templates for different file types
        self.code_templates = {
            'python': [
                self._generate_python_function,
                self._generate_python_class,
                self._generate_python_script
            ],
            'javascript': [
                self._generate_js_function,
                self._generate_js_class,
                self._generate_js_module
            ],
            'html': [
                self._generate_html_page
            ],
            'css': [
                self._generate_css_styles
            ]
        }
        
        # Common programming words for generating realistic variable names
        self.code_words = [
            'data', 'result', 'value', 'item', 'element', 'node', 'list', 'array',
            'string', 'number', 'count', 'index', 'key', 'name', 'id', 'type',
            'status', 'config', 'options', 'params', 'args', 'response', 'request'
        ]
    
    def _random_variable_name(self):
        """Generate a random but realistic variable name"""
        return random.choice(self.code_words) + '_' + ''.join(random.choices(string.ascii_lowercase, k=3))
    
    def _random_function_name(self):
        """Generate a random function name"""
        verbs = ['get', 'set', 'create', 'update', 'delete', 'process', 'handle', 'check', 'validate']
        nouns = ['data', 'user', 'item', 'config', 'response', 'request', 'value', 'result']
        return random.choice(verbs) + '_' + random.choice(nouns)
    
    def _generate_python_function(self):
        """Generate a random Python function"""
        func_name = self._random_function_name()
        param1 = self._random_variable_name()
        param2 = self._random_variable_name()
        var_name = self._random_variable_name()
        
        return f'''def {func_name}({param1}, {param2}=None):
    """
    Randomly generated function that processes {param1}
    """
    {var_name} = []
    
    if {param2} is None:
        {param2} = {random.randint(1, 100)}
    
    for i in range({param2}):
        {var_name}.append({param1} + str(i))
    
    return {var_name}

# Example usage
if __name__ == "__main__":
    result = {func_name}("test", {random.randint(1, 10)})
    print(f"Generated {{len(result)}} items")
'''
    
    def _generate_python_class(self):
        """Generate a random Python class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        attr1 = self._random_variable_name()
        attr2 = self._random_variable_name()
        
        return f'''class {class_name}:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, {attr1}, {attr2}={random.randint(1, 100)}):
        self.{attr1} = {attr1}
        self.{attr2} = {attr2}
        self.created_at = "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    def get_info(self):
        return {{
            "{attr1}": self.{attr1},
            "{attr2}": self.{attr2},
            "created_at": self.created_at
        }}
    
    def update_{attr1}(self, new_value):
        old_value = self.{attr1}
        self.{attr1} = new_value
        return f"Updated from {{old_value}} to {{new_value}}"

# Example usage
obj = {class_name}("sample_data", {random.randint(10, 50)})
print(obj.get_info())
'''
    
    def _generate_python_script(self):
        """Generate a random Python script"""
        var1 = self._random_variable_name()
        var2 = self._random_variable_name()
        
        return f'''#!/usr/bin/env python3
"""
Random utility script generated on {datetime.now().strftime('%Y-%m-%d')}
"""

import random
import json
from datetime import datetime

# Configuration
{var1.upper()} = {random.randint(10, 100)}
{var2.upper()} = "{random.choice(['development', 'production', 'testing'])}"

def main():
    """Main execution function"""
    print(f"Starting process with {var1.upper()}: {{{var1.upper()}}}")
    print(f"Environment: {{{var2.upper()}}}")
    
    # Generate some random data
    data = []
    for i in range({var1.upper()}):
        item = {{
            "id": i + 1,
            "value": random.randint(1, 1000),
            "timestamp": datetime.now().isoformat(),
            "active": random.choice([True, False])
        }}
        data.append(item)
    
    # Process the data
    active_items = [item for item in data if item["active"]]
    total_value = sum(item["value"] for item in active_items)
    
    print(f"Generated {{len(data)}} items")
    print(f"Active items: {{len(active_items)}}")
    print(f"Total value: {{total_value}}")
    
    return data

if __name__ == "__main__":
    result = main()
    print("Process completed successfully!")
'''
    
    def _generate_js_function(self):
        """Generate a random JavaScript function"""
        func_name = self._random_function_name()
        param = self._random_variable_name()
        
        return f'''// Random JavaScript function generated on {datetime.now().strftime('%Y-%m-%d')}

function {func_name}({param}) {{
    const result = [];
    const multiplier = {random.randint(2, 10)};
    
    if (!Array.isArray({param})) {{
        {param} = [{param}];
    }}
    
    {param}.forEach((item, index) => {{
        result.push({{
            original: item,
            processed: item * multiplier,
            index: index,
            timestamp: new Date().toISOString()
        }});
    }});
    
    return result;
}}

// Example usage
const testData = [{', '.join(str(random.randint(1, 100)) for _ in range(5))}];
const processed = {func_name}(testData);
console.log('Processed data:', processed);

module.exports = {func_name};
'''
    
    def _generate_js_class(self):
        """Generate a random JavaScript class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random JavaScript class generated on {datetime.now().strftime('%Y-%m-%d')}

class {class_name} {{
    constructor(initialValue = {random.randint(1, 100)}) {{
        this.value = initialValue;
        this.history = [];
        this.createdAt = new Date();
    }}
    
    update(newValue) {{
        this.history.push({{
            oldValue: this.value,
            newValue: newValue,
            timestamp: new Date()
        }});
        this.value = newValue;
        return this;
    }}
    
    getStats() {{
        return {{
            currentValue: this.value,
            historyLength: this.history.length,
            createdAt: this.createdAt,
            lastUpdate: this.history.length > 0 ? this.history[this.history.length - 1].timestamp : null
        }};
    }}
    
    reset() {{
        this.value = 0;
        this.history = [];
        return this;
    }}
}}

// Example usage
const instance = new {class_name}({random.randint(10, 50)});
instance.update({random.randint(51, 100)});
console.log('Stats:', instance.getStats());

module.exports = {class_name};
'''
    
    def _generate_js_module(self):
        """Generate a random JavaScript module"""
        module_name = self._random_function_name()
        
        return f'''// Random JavaScript module: {module_name}
// Generated on {datetime.now().strftime('%Y-%m-%d')}

const {module_name} = {{
    version: "1.0.{random.randint(0, 99)}",
    
    config: {{
        timeout: {random.randint(1000, 5000)},
        retries: {random.randint(1, 5)},
        debug: {random.choice(['true', 'false'])}
    }},
    
    utils: {{
        generateId: () => Math.random().toString(36).substr(2, 9),
        
        formatDate: (date = new Date()) => {{
            return date.toISOString().split('T')[0];
        }},
        
        processArray: (arr, callback) => {{
            if (!Array.isArray(arr)) return [];
            return arr.map((item, index) => callback(item, index));
        }}
    }},
    
    async fetchData(url) {{
        const maxRetries = this.config.retries;
        let attempt = 0;
        
        while (attempt < maxRetries) {{
            try {{
                // Simulated async operation
                await new Promise(resolve => setTimeout(resolve, 100));
                return {{
                    success: true,
                    data: `Mock data from ${{url}}`,
                    attempt: attempt + 1,
                    timestamp: new Date().toISOString()
                }};
            }} catch (error) {{
                attempt++;
                if (attempt >= maxRetries) throw error;
            }}
        }}
    }}
}};

module.exports = {module_name};
'''
    
    def _generate_html_page(self):
        """Generate a random HTML page"""
        title = f"Random Page {random.randint(1000, 9999)}"
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #{random.randint(240, 255):02x}{random.randint(240, 255):02x}{random.randint(240, 255):02x};
        }}
        .header {{
            background-color: #{random.randint(50, 150):02x}{random.randint(50, 150):02x}{random.randint(50, 150):02x};
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .content {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p>Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}</p>
    </div>
    
    <div class="content">
        <h2>Random Content Section</h2>
        <p>This page was automatically generated with random content.</p>
        
        <h3>Random List</h3>
        <ul>
            {''.join(f'<li>Item {i}: {random.choice(["Important", "Optional", "Required", "Recommended"])} - {random.randint(1, 100)}%</li>' for i in range(1, random.randint(4, 8)))}
        </ul>
        
        <h3>Random Data</h3>
        <table border="1" style="border-collapse: collapse; width: 100%;">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Value</th>
                <th>Status</th>
            </tr>
            {''.join(f'<tr><td>{i}</td><td>Item_{i}</td><td>{random.randint(100, 999)}</td><td>{random.choice(["Active", "Inactive", "Pending"])}</td></tr>' for i in range(1, 6))}
        </table>
    </div>
    
    <script>
        console.log('Page loaded at:', new Date().toISOString());
        document.addEventListener('DOMContentLoaded', function() {{
            console.log('DOM content loaded');
        }});
    </script>
</body>
</html>
'''
    
    def _generate_css_styles(self):
        """Generate random CSS styles"""
        return f'''/* Random CSS styles generated on {datetime.now().strftime('%Y-%m-%d')} */

:root {{
    --primary-color: #{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x};
    --secondary-color: #{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x};
    --accent-color: #{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x};
    --font-size-base: {random.randint(14, 18)}px;
    --border-radius: {random.randint(4, 12)}px;
}}

.random-container {{
    max-width: {random.randint(800, 1200)}px;
    margin: 0 auto;
    padding: {random.randint(10, 30)}px;
    background: linear-gradient({random.randint(0, 360)}deg, var(--primary-color), var(--secondary-color));
    border-radius: var(--border-radius);
}}

.random-card {{
    background: white;
    padding: {random.randint(15, 25)}px;
    margin: {random.randint(10, 20)}px 0;
    border-radius: var(--border-radius);
    box-shadow: 0 {random.randint(2, 6)}px {random.randint(8, 16)}px rgba(0, 0, 0, 0.{random.randint(1, 3)});
    transition: transform 0.{random.randint(2, 5)}s ease;
}}

.random-card:hover {{
    transform: translateY(-{random.randint(2, 8)}px);
}}

.random-button {{
    background: var(--accent-color);
    color: white;
    border: none;
    padding: {random.randint(8, 16)}px {random.randint(16, 32)}px;
    border-radius: var(--border-radius);
    cursor: pointer;
    font-size: var(--font-size-base);
    transition: all 0.3s ease;
}}

.random-button:hover {{
    opacity: 0.{random.randint(7, 9)};
    transform: scale(1.0{random.randint(1, 5)});
}}

.random-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax({random.randint(200, 300)}px, 1fr));
    gap: {random.randint(15, 25)}px;
    margin: {random.randint(20, 40)}px 0;
}}

@media (max-width: {random.randint(600, 800)}px) {{
    .random-container {{
        padding: {random.randint(10, 20)}px;
    }}
    
    .random-grid {{
        grid-template-columns: 1fr;
    }}
}}
'''
    
    def generate_random_code(self):
        """Generate random code file"""
        # Choose random file type
        file_type = random.choice(list(self.code_templates.keys()))
        
        # Choose random template for that file type
        template_func = random.choice(self.code_templates[file_type])
        
        # Generate the code
        code_content = template_func()
        
        # Generate filename
        base_name = self._random_function_name()
        extensions = {
            'python': '.py',
            'javascript': '.js',
            'html': '.html',
            'css': '.css'
        }
        
        filename = f"{base_name}{extensions[file_type]}"
        
        return filename, code_content, file_type
    
    def generate_commit_message(self, filename, file_type):
        """Generate a commit message based on the generated code"""
        actions = [
            "Add", "Create", "Implement", "Generate", "Build", "Develop",
            "Update", "Refactor", "Optimize", "Enhance"
        ]
        
        descriptions = {
            'python': [
                "utility function", "data processor", "helper module", "automation script",
                "class implementation", "API handler", "configuration manager"
            ],
            'javascript': [
                "frontend component", "utility function", "module export", "DOM handler",
                "event processor", "data transformer", "API client"
            ],
            'html': [
                "webpage template", "UI layout", "responsive design", "landing page",
                "component structure", "form interface"
            ],
            'css': [
                "styling system", "responsive layout", "component styles", "theme colors",
                "animation effects", "grid layout", "utility classes"
            ]
        }
        
        action = random.choice(actions)
        description = random.choice(descriptions[file_type])
        
        # Add some variety to commit messages
        message_formats = [
            f"{action} {description} in {filename}",
            f"{action} new {description} ({filename})",
            f"{action} {description} - {filename}",
            f"✨ {action} {description}",
            f"🚀 {action} {description} for improved functionality",
            f"⚡ {action} optimized {description}",
            f"🔧 {action} {description} with enhanced features"
        ]
        
        return random.choice(message_formats)
    
    def create_and_commit_file(self):
        """Generate code, create file, and commit to git"""
        try:
            # Generate random code
            filename, code_content, file_type = self.generate_random_code()
            
            # Create full file path
            file_path = os.path.join(self.repo_path, filename)
            
            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code_content)
            
            print(f"✅ Created file: {filename}")
            
            # Change to repo directory
            original_dir = os.getcwd()
            os.chdir(self.repo_path)
            
            try:
                # Add all files to git (git add .)
                subprocess.run(['git', 'add', '.'], check=True)
                
                # Generate automated commit message
                commit_message = self.generate_commit_message(filename, file_type)
                
                # Commit with automated message
                subprocess.run(['git', 'commit', '-m', commit_message], check=True)
                print(f"✅ Committed: {commit_message}")
                
                # Push to remote
                subprocess.run(['git', 'push'], check=True)
                print(f"✅ Pushed to remote repository")
                
                return True, filename, commit_message
                
            finally:
                os.chdir(original_dir)
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Git command failed: {e}")
            return False, None, None
        except Exception as e:
            print(f"❌ Error: {e}")
            return False, None, None
    
    def run_continuous(self, interval_minutes=30, max_commits=None):
        """Run the generator continuously"""
        import time
        
        commit_count = 0
        print(f"🚀 Starting random code generator...")
        print(f"📁 Repository: {self.repo_path}")
        print(f"⏰ Interval: {interval_minutes} minutes")
        if max_commits:
            print(f"🎯 Max commits: {max_commits}")
        print("=" * 50)
        
        while True:
            try:
                success, filename, commit_message = self.create_and_commit_file()
                
                if success:
                    commit_count += 1
                    print(f"📊 Total commits: {commit_count}")
                    
                    if max_commits and commit_count >= max_commits:
                        print(f"🎉 Reached maximum commits ({max_commits}). Stopping.")
                        break
                else:
                    print("⚠️ Commit failed, continuing...")
                
                print(f"😴 Waiting {interval_minutes} minutes until next commit...")
                print("=" * 50)
                
                time.sleep(interval_minutes * 60)  # Convert to seconds
                
            except KeyboardInterrupt:
                print("\n🛑 Stopped by user")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                print(f"⏳ Waiting {interval_minutes} minutes before retry...")
                time.sleep(interval_minutes * 60)

def main():
    """Main function to run the random code generator"""
    
    # Automatic configuration - no user input required
    REPO_PATH = os.getcwd()  # Use current directory
    REMOTE_URL = "https://github.com/jex23/radom_code.git"
    INTERVAL_MINUTES = 5  # Commit every 5 minutes
    MAX_COMMITS = None  # Unlimited commits (set to a number to limit)
    
    print("🚀 Starting automated random code generator...")
    print(f"📁 Repository: {REPO_PATH}")
    print(f"🌐 Remote: {REMOTE_URL}")
    print(f"⏰ Interval: {INTERVAL_MINUTES} minutes")
    
    # Check if it's a git repository, if not, initialize and set remote
    if not os.path.exists(os.path.join(REPO_PATH, '.git')):
        print("🔧 Initializing git repository...")
        os.chdir(REPO_PATH)
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'remote', 'add', 'origin', REMOTE_URL], check=True)
        print("✅ Git repository initialized and remote added!")
    else:
        print("✅ Git repository found!")
    
    # Create generator instance
    generator = RandomCodeGenerator(REPO_PATH)
    
    # Run continuously
    generator.run_continuous(INTERVAL_MINUTES, MAX_COMMITS)

if __name__ == "__main__":
    main()