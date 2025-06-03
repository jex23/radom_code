import os
import random
import string
import subprocess
import json
from datetime import datetime
import shutil

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
            'typescript': [
                self._generate_ts_function,
                self._generate_ts_class,
                self._generate_ts_interface
            ],
            'dart': [
                self._generate_dart_function,
                self._generate_dart_class,
                self._generate_dart_widget
            ],
            'ruby': [
                self._generate_ruby_function,
                self._generate_ruby_class,
                self._generate_ruby_module
            ],
            'go': [
                self._generate_go_function,
                self._generate_go_struct,
                self._generate_go_package
            ],
            'cpp': [
                self._generate_cpp_function,
                self._generate_cpp_class,
                self._generate_cpp_header
            ],
            'c': [
                self._generate_c_function,
                self._generate_c_struct,
                self._generate_c_header
            ],
            'csharp': [
                self._generate_csharp_function,
                self._generate_csharp_class,
                self._generate_csharp_interface
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
    
    def _generate_ts_function(self):
        """Generate a random TypeScript function"""
        func_name = self._random_function_name()
        param = self._random_variable_name()
        interface_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random TypeScript function generated on {datetime.now().strftime('%Y-%m-%d')}

interface {interface_name} {{
    id: number;
    name: string;
    value: number;
    active: boolean;
}}

function {func_name}({param}: {interface_name}[]): {interface_name}[] {{
    const multiplier: number = {random.randint(2, 10)};
    
    return {param}
        .filter((item: {interface_name}) => item.active)
        .map((item: {interface_name}, index: number) => ({{
            ...item,
            value: item.value * multiplier
        }}));
}}

// Example usage
const testData: {interface_name}[] = [
    {{ id: 1, name: "Item1", value: {random.randint(10, 100)}, active: true }},
    {{ id: 2, name: "Item2", value: {random.randint(10, 100)}, active: false }}
];

const result = {func_name}(testData);
console.log('Processed items:', result);

export {{ {func_name}, {interface_name} }};
'''
    
    def _generate_ts_class(self):
        """Generate a random TypeScript class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random TypeScript class generated on {datetime.now().strftime('%Y-%m-%d')}

class {class_name} {{
    private value: number;
    private readonly createdAt: Date;

    constructor(initialValue: number = {random.randint(1, 100)}) {{
        this.value = initialValue;
        this.createdAt = new Date();
    }}

    public getValue(): number {{
        return this.value;
    }}

    public updateValue(newValue: number): void {{
        this.value = newValue;
    }}

    public getInfo(): object {{
        return {{
            value: this.value,
            createdAt: this.createdAt.toISOString()
        }};
    }}
}}

export {{ {class_name} }};
'''
    
    def _generate_ts_interface(self):
        """Generate a random TypeScript interface"""
        interface_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random TypeScript interface generated on {datetime.now().strftime('%Y-%m-%d')}

interface {interface_name} {{
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {{
        version: number;
        lastUpdated: Date;
    }};
}}

type {interface_name}Response = {{
    success: boolean;
    data?: {interface_name};
    error?: string;
}};

export {{ {interface_name}, {interface_name}Response }};
'''
    
    def _generate_dart_function(self):
        """Generate a random Dart function"""
        func_name = self._random_function_name()
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random Dart function generated on {datetime.now().strftime('%Y-%m-%d')}

class {class_name} {{
  final int id;
  final String name;
  final double value;

  const {class_name}({{
    required this.id,
    required this.name,
    required this.value,
  }});
}}

List<{class_name}> {func_name}(List<{class_name}> items) {{
  const double multiplier = {random.randint(2, 10)}.0;
  
  return items
      .map((item) => {class_name}(
            id: item.id,
            name: '${{item.name}}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}}

void main() {{
  final testData = [
    {class_name}(id: 1, name: 'Item1', value: {random.randint(10, 100)}.0),
  ];

  final result = {func_name}(testData);
  print('Processed ${{result.length}} items');
}}
'''
    
    def _generate_dart_class(self):
        """Generate a random Dart class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random Dart class generated on {datetime.now().strftime('%Y-%m-%d')}

class {class_name} {{
  String _name;
  int _value;

  {class_name}(this._name, this._value);

  String get name => _name;
  int get value => _value;

  set name(String newName) {{
    _name = newName;
  }}

  set value(int newValue) {{
    _value = newValue;
  }}

  Map<String, dynamic> toJson() {{
    return {{
      'name': _name,
      'value': _value,
    }};
  }}
}}
'''
    
    def _generate_dart_widget(self):
        """Generate a random Dart widget"""
        widget_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random Flutter widget generated on {datetime.now().strftime('%Y-%m-%d')}

import 'package:flutter/material.dart';

class {widget_name} extends StatelessWidget {{
  final String title;
  final int value;

  const {widget_name}({{
    Key? key,
    required this.title,
    this.value = {random.randint(1, 100)},
  }}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return Container(
      padding: EdgeInsets.all(16.0),
      child: Column(
        children: [
          Text(title, style: TextStyle(fontSize: 18)),
          Text('Value: $value', style: TextStyle(fontSize: 14)),
        ],
      ),
    );
  }}
}}
'''
    
    def _generate_ruby_function(self):
        """Generate a random Ruby function"""
        func_name = self._random_function_name()
        
        return f'''# Random Ruby function generated on {datetime.now().strftime('%Y-%m-%d')}

def {func_name}(items, multiplier = {random.randint(2, 10)})
  return [] if items.nil? || items.empty?
  
  items.map.with_index do |item, index|
    {{
      original: item,
      processed: item * multiplier,
      index: index,
      timestamp: Time.now.iso8601
    }}
  end
end

# Example usage
test_data = [{', '.join(str(random.randint(1, 100)) for _ in range(5))}]
result = {func_name}(test_data)
puts "Processed #{{result.length}} items"
'''
    
    def _generate_ruby_class(self):
        """Generate a random Ruby class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''# Random Ruby class generated on {datetime.now().strftime('%Y-%m-%d')}

class {class_name}
  attr_reader :name, :value, :created_at
  attr_writer :name, :value

  def initialize(name, value = {random.randint(1, 100)})
    @name = name
    @value = value
    @created_at = Time.now
  end

  def to_hash
    {{
      name: @name,
      value: @value,
      created_at: @created_at.iso8601
    }}
  end

  def update_value(new_value)
    old_value = @value
    @value = new_value
    "Updated from #{{old_value}} to #{{new_value}}"
  end
end

# Example usage
obj = {class_name}.new("sample", {random.randint(10, 50)})
puts obj.to_hash
'''
    
    def _generate_ruby_module(self):
        """Generate a random Ruby module"""
        module_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''# Random Ruby module generated on {datetime.now().strftime('%Y-%m-%d')}

module {module_name}
  VERSION = "1.0.{random.randint(0, 99)}"
  
  def self.process_data(data)
    return [] unless data.is_a?(Array)
    
    data.map do |item|
      {{
        original: item,
        processed: item.to_s.upcase,
        timestamp: Time.now.iso8601
      }}
    end
  end
  
  def self.generate_id
    Time.now.to_f.to_s.gsub('.', '')
  end
end

# Example usage
puts {module_name}::VERSION
result = {module_name}.process_data(['test', 'data'])
puts result
'''
    
    def _generate_go_function(self):
        """Generate a random Go function"""
        func_name = self._random_function_name()
        
        return f'''// Random Go function generated on {datetime.now().strftime('%Y-%m-%d')}
package main

import (
    "fmt"
    "time"
)

type Item struct {{
    ID        int       `json:"id"`
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    CreatedAt time.Time `json:"created_at"`
}}

func {func_name}(items []Item) []Item {{
    multiplier := {random.randint(2, 10)}
    result := make([]Item, len(items))
    
    for i, item := range items {{
        result[i] = Item{{
            ID:        item.ID,
            Name:      fmt.Sprintf("%s_processed", item.Name),
            Value:     item.Value * multiplier,
            CreatedAt: time.Now(),
        }}
    }}
    
    return result
}}

func main() {{
    testData := []Item{{
        {{ID: 1, Name: "item1", Value: {random.randint(10, 100)}, CreatedAt: time.Now()}},
        {{ID: 2, Name: "item2", Value: {random.randint(10, 100)}, CreatedAt: time.Now()}},
    }}
    
    result := {func_name}(testData)
    fmt.Printf("Processed %d items\\n", len(result))
}}
'''
    
    def _generate_go_struct(self):
        """Generate a random Go struct"""
        struct_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random Go struct generated on {datetime.now().strftime('%Y-%m-%d')}
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type {struct_name} struct {{
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}}

func New{struct_name}(name string, value int) *{struct_name} {{
    return &{struct_name}{{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }}
}}

func (s *{struct_name}) UpdateValue(newValue int) {{
    s.Value = newValue
}}

func (s *{struct_name}) ToJSON() ([]byte, error) {{
    return json.Marshal(s)
}}

func main() {{
    obj := New{struct_name}("sample", {random.randint(10, 100)})
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}}
'''
    
    def _generate_go_package(self):
        """Generate a random Go package"""
        package_name = self._random_function_name()
        
        return f'''// Random Go package generated on {datetime.now().strftime('%Y-%m-%d')}
package {package_name}

import (
    "fmt"
    "time"
)

const Version = "1.0.{random.randint(0, 99)}"

type Config struct {{
    Timeout time.Duration `json:"timeout"`
    Retries int          `json:"retries"`
    Debug   bool         `json:"debug"`
}}

func NewConfig() *Config {{
    return &Config{{
        Timeout: {random.randint(1, 10)} * time.Second,
        Retries: {random.randint(1, 5)},
        Debug:   false,
    }}
}}

func ProcessItems(items []interface{{}}) []map[string]interface{{}} {{
    var result []map[string]interface{{}}
    
    for i, item := range items {{
        processed := map[string]interface{{}}{{
            "original":  item,
            "index":     i,
            "timestamp": time.Now().Unix(),
            "processed": true,
        }}
        result = append(result, processed)
    }}
    
    return result
}}

func GetVersion() string {{
    return fmt.Sprintf("Package %s version %s", "{package_name}", Version)
}}
'''
    
    def _generate_cpp_function(self):
        """Generate a random C++ function"""
        func_name = self._random_function_name()
        
        return f'''// Random C++ function generated on {datetime.now().strftime('%Y-%m-%d')}
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

struct Item {{
    int id;
    std::string name;
    double value;
    
    Item(int id, const std::string& name, double value) 
        : id(id), name(name), value(value) {{}}
}};

std::vector<Item> {func_name}(const std::vector<Item>& items) {{
    const double multiplier = {random.randint(2, 10)}.0;
    std::vector<Item> result;
    
    std::transform(items.begin(), items.end(), std::back_inserter(result),
        [multiplier](const Item& item) {{
            return Item(item.id, item.name + "_processed", item.value * multiplier);
        }});
    
    return result;
}}

int main() {{
    std::vector<Item> testData = {{
        Item(1, "item1", {random.randint(10, 100)}.0),
        Item(2, "item2", {random.randint(10, 100)}.0)
    }};
    
    auto result = {func_name}(testData);
    std::cout << "Processed " << result.size() << " items" << std::endl;
    
    return 0;
}}
'''
    
    def _generate_cpp_class(self):
        """Generate a random C++ class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random C++ class generated on {datetime.now().strftime('%Y-%m-%d')}
#include <iostream>
#include <string>
#include <vector>

class {class_name} {{
private:
    std::string name_;
    int value_;
    std::vector<std::string> history_;

public:
    {class_name}(const std::string& name, int value = {random.randint(1, 100)}) 
        : name_(name), value_(value) {{}}
    
    void setName(const std::string& name) {{
        history_.push_back("Name changed from " + name_ + " to " + name);
        name_ = name;
    }}
    
    void setValue(int value) {{
        history_.push_back("Value changed from " + std::to_string(value_) + " to " + std::to_string(value));
        value_ = value;
    }}
    
    std::string getName() const {{ return name_; }}
    int getValue() const {{ return value_; }}
    
    void printHistory() const {{
        for (const auto& entry : history_) {{
            std::cout << entry << std::endl;
        }}
    }}
}};

int main() {{
    {class_name} obj("sample", {random.randint(10, 50)});
    obj.setValue({random.randint(51, 100)});
    obj.printHistory();
    
    return 0;
}}
'''
    
    def _generate_cpp_header(self):
        """Generate a random C++ header"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random C++ header generated on {datetime.now().strftime('%Y-%m-%d')}
#ifndef {class_name.upper()}_H
#define {class_name.upper()}_H

#include <string>
#include <vector>
#include <memory>

namespace utils {{

template<typename T>
class {class_name} {{
private:
    std::vector<T> data_;
    std::string name_;

public:
    explicit {class_name}(const std::string& name);
    ~{class_name}() = default;
    
    void add(const T& item);
    void remove(size_t index);
    T& get(size_t index);
    const T& get(size_t index) const;
    
    size_t size() const {{ return data_.size(); }}
    bool empty() const {{ return data_.empty(); }}
    
    void clear();
    std::string getName() const {{ return name_; }}
}};

// Template implementation
template<typename T>
{class_name}<T>::{class_name}(const std::string& name) : name_(name) {{}}

template<typename T>
void {class_name}<T>::add(const T& item) {{
    data_.push_back(item);
}}

template<typename T>
void {class_name}<T>::remove(size_t index) {{
    if (index < data_.size()) {{
        data_.erase(data_.begin() + index);
    }}
}}

template<typename T>
T& {class_name}<T>::get(size_t index) {{
    return data_.at(index);
}}

template<typename T>
const T& {class_name}<T>::get(size_t index) const {{
    return data_.at(index);
}}

template<typename T>
void {class_name}<T>::clear() {{
    data_.clear();
}}

}} // namespace utils

#endif // {class_name.upper()}_H
'''
    
    def _generate_c_function(self):
        """Generate a random C function"""
        func_name = self._random_function_name()
        
        return f'''// Random C function generated on {datetime.now().strftime('%Y-%m-%d')}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {{
    int id;
    char name[50];
    double value;
}} Item;

Item* {func_name}(const Item* items, int count, int* result_count) {{
    const double multiplier = {random.randint(2, 10)}.0;
    Item* result = malloc(count * sizeof(Item));
    
    if (result == NULL) {{
        *result_count = 0;
        return NULL;
    }}
    
    for (int i = 0; i < count; i++) {{
        result[i].id = items[i].id;
        snprintf(result[i].name, sizeof(result[i].name), "%s_processed", items[i].name);
        result[i].value = items[i].value * multiplier;
    }}
    
    *result_count = count;
    return result;
}}

int main() {{
    Item testData[] = {{
        {{1, "item1", {random.randint(10, 100)}.0}},
        {{2, "item2", {random.randint(10, 100)}.0}}
    }};
    
    int result_count;
    Item* result = {func_name}(testData, 2, &result_count);
    
    printf("Processed %d items\\n", result_count);
    
    if (result) {{
        free(result);
    }}
    
    return 0;
}}
'''
    
    def _generate_c_struct(self):
        """Generate a random C struct"""
        struct_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random C struct generated on {datetime.now().strftime('%Y-%m-%d')}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {{
    char name[100];
    int value;
    int active;
    long timestamp;
}} {struct_name};

{struct_name}* create_{struct_name.lower()}(const char* name, int value) {{
    {struct_name}* obj = malloc(sizeof({struct_name}));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = {random.randint(1000000000, 2000000000)};
    
    return obj;
}}

void update_{struct_name.lower()}_value({struct_name}* obj, int new_value) {{
    if (obj != NULL) {{
        obj->value = new_value;
    }}
}}

void print_{struct_name.lower()}(const {struct_name}* obj) {{
    if (obj != NULL) {{
        printf("Name: %s, Value: %d, Active: %d\\n", 
               obj->name, obj->value, obj->active);
    }}
}}

void free_{struct_name.lower()}({struct_name}* obj) {{
    if (obj != NULL) {{
        free(obj);
    }}
}}

int main() {{
    {struct_name}* obj = create_{struct_name.lower()}("sample", {random.randint(10, 100)});
    print_{struct_name.lower()}(obj);
    free_{struct_name.lower()}(obj);
    
    return 0;
}}
'''
    
    def _generate_c_header(self):
        """Generate a random C header"""
        module_name = self._random_function_name()
        
        return f'''// Random C header generated on {datetime.now().strftime('%Y-%m-%d')}
#ifndef {module_name.upper()}_H
#define {module_name.upper()}_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {{
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE {random.randint(512, 2048)}

typedef enum {{
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
}} {module_name}_status_t;

typedef struct {{
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
}} {module_name}_item_t;

typedef struct {{
    {module_name}_item_t* items;
    size_t count;
    size_t capacity;
}} {module_name}_collection_t;

// Function declarations
{module_name}_status_t {module_name}_init({module_name}_collection_t* collection);
{module_name}_status_t {module_name}_add_item({module_name}_collection_t* collection, 
                                              const {module_name}_item_t* item);
{module_name}_status_t {module_name}_remove_item({module_name}_collection_t* collection, 
                                                 int id);
{module_name}_item_t* {module_name}_find_item({module_name}_collection_t* collection, 
                                              int id);
void {module_name}_cleanup({module_name}_collection_t* collection);

// Utility functions
const char* {module_name}_status_string({module_name}_status_t status);
size_t {module_name}_get_count(const {module_name}_collection_t* collection);

#ifdef __cplusplus
}}
#endif

#endif // {module_name.upper()}_H
'''
    
    def _generate_csharp_function(self):
        """Generate a random C# function"""
        func_name = self._random_function_name()
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random C# function generated on {datetime.now().strftime('%Y-%m-%d')}
using System;
using System.Collections.Generic;
using System.Linq;

public class {class_name}
{{
    public int Id {{ get; set; }}
    public string Name {{ get; set; }}
    public double Value {{ get; set; }}
    public DateTime CreatedAt {{ get; set; }}
    
    public {class_name}(int id, string name, double value)
    {{
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }}
}}

public static class {func_name.capitalize()}Processor
{{
    public static List<{class_name}> {func_name.capitalize()}(IEnumerable<{class_name}> items)
    {{
        const double multiplier = {random.randint(2, 10)}.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new {class_name}(
                item.Id,
                $"{{item.Name}}_processed",
                item.Value * multiplier))
            .ToList();
    }}
    
    public static void Main()
    {{
        var testData = new List<{class_name}>
        {{
            new {class_name}(1, "Item1", {random.randint(10, 100)}),
            new {class_name}(2, "Item2", {random.randint(10, 100)})
        }};
        
        var result = {func_name.capitalize()}(testData);
        Console.WriteLine($"Processed {{result.Count}} items");
    }}
}}
'''
    
    def _generate_csharp_class(self):
        """Generate a random C# class"""
        class_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random C# class generated on {datetime.now().strftime('%Y-%m-%d')}
using System;
using System.Collections.Generic;
using System.ComponentModel;

public class {class_name} : INotifyPropertyChanged
{{
    private string _name;
    private int _value;
    private readonly List<string> _history;
    
    public event PropertyChangedEventHandler PropertyChanged;
    
    public {class_name}(string name, int value = {random.randint(1, 100)})
    {{
        _name = name;
        _value = value;
        _history = new List<string>();
        CreatedAt = DateTime.Now;
        AddToHistory($"Created with name: {{name}}, value: {{value}}");
    }}
    
    public string Name
    {{
        get => _name;
        set
        {{
            if (_name != value)
            {{
                var oldValue = _name;
                _name = value;
                AddToHistory($"Name changed from {{oldValue}} to {{value}}");
                OnPropertyChanged(nameof(Name));
            }}
        }}
    }}
    
    public int Value
    {{
        get => _value;
        set
        {{
            if (_value != value)
            {{
                var oldValue = _value;
                _value = value;
                AddToHistory($"Value changed from {{oldValue}} to {{value}}");
                OnPropertyChanged(nameof(Value));
            }}
        }}
    }}
    
    public DateTime CreatedAt {{ get; }}
    
    public IReadOnlyList<string> History => _history.AsReadOnly();
    
    private void AddToHistory(string entry)
    {{
        _history.Add($"{{DateTime.Now:yyyy-MM-dd HH:mm:ss}} - {{entry}}");
    }}
    
    protected virtual void OnPropertyChanged(string propertyName)
    {{
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }}
    
    public override string ToString()
    {{
        return $"{class_name} {{ Name = {{Name}}, Value = {{Value}}, CreatedAt = {{CreatedAt}} }}";
    }}
}}
'''
    
    def _generate_csharp_interface(self):
        """Generate a random C# interface"""
        interface_name = ''.join(word.capitalize() for word in self._random_function_name().split('_'))
        
        return f'''// Random C# interface generated on {datetime.now().strftime('%Y-%m-%d')}
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface I{interface_name}<T> where T : class
{{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}}

public class {interface_name}Entity
{{
    public int Id {{ get; set; }}
    public string Name {{ get; set; }}
    public string Status {{ get; set; }}
    public DateTime CreatedAt {{ get; set; }}
    public DateTime? UpdatedAt {{ get; set; }}
}}

public class {interface_name}Service : I{interface_name}<{interface_name}Entity>
{{
    private readonly Dictionary<int, {interface_name}Entity> _storage;
    private int _nextId;
    
    public {interface_name}Service()
    {{
        _storage = new Dictionary<int, {interface_name}Entity>();
        _nextId = 1;
    }}
    
    public async Task<{interface_name}Entity> CreateAsync({interface_name}Entity entity)
    {{
        await Task.Delay({random.randint(10, 100)});
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }}
    
    public async Task<{interface_name}Entity> GetByIdAsync(int id)
    {{
        await Task.Delay({random.randint(10, 50)});
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }}
    
    public async Task<IEnumerable<{interface_name}Entity>> GetAllAsync()
    {{
        await Task.Delay({random.randint(20, 100)});
        return _storage.Values;
    }}
    
    public async Task<{interface_name}Entity> UpdateAsync({interface_name}Entity entity)
    {{
        await Task.Delay({random.randint(10, 80)});
        
        if (_storage.ContainsKey(entity.Id))
        {{
            entity.UpdatedAt = DateTime.Now;
            _storage[entity.Id] = entity;
            return entity;
        }}
        
        return null;
    }}
    
    public async Task<bool> DeleteAsync(int id)
    {{
        await Task.Delay({random.randint(10, 60)});
        return _storage.Remove(id);
    }}
    
    public async Task<int> CountAsync()
    {{
        await Task.Delay({random.randint(5, 30)});
        return _storage.Count;
    }}
}}
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

    def _generate_unique_filename(self, file_type, max_attempts=10):
        """Generate a unique filename that doesn't exist in the repository"""
        extensions = {
            'python': '.py',
            'javascript': '.js',
            'typescript': '.ts',
            'dart': '.dart',
            'ruby': '.rb',
            'go': '.go',
            'cpp': '.cpp',
            'c': '.c',
            'csharp': '.cs',
            'html': '.html',
            'css': '.css'
        }
        
        for attempt in range(max_attempts):
            base_name = self._random_function_name()
            filename = f"{base_name}{extensions[file_type]}"
            file_path = os.path.join(self.repo_path, filename)
            
            # If file doesn't exist, we can use this filename
            if not os.path.exists(file_path):
                return filename
            
            print(f"[WARNING] File {filename} already exists, generating new name... (attempt {attempt + 1})")
        
        # If we couldn't find a unique name after max_attempts, add timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = self._random_function_name()
        filename = f"{base_name}_{timestamp}{extensions[file_type]}"
        return filename
    
    def _backup_existing_file(self, filename):
        """Create a backup of existing file before overwriting"""
        file_path = os.path.join(self.repo_path, filename)
        if os.path.exists(file_path):
            # Create backup directory if it doesn't exist
            backup_dir = os.path.join(self.repo_path, 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            
            # Generate backup filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"{os.path.splitext(filename)[0]}_{timestamp}_backup{os.path.splitext(filename)[1]}"
            backup_path = os.path.join(backup_dir, backup_filename)
            
            # Copy file to backup
            shutil.copy2(file_path, backup_path)
            print(f"[BACKUP] Backed up existing {filename} to backups/{backup_filename}")
            return backup_path
        return None

    def generate_random_code(self):
        """Generate random code file with unique filename"""
        # Choose random file type
        file_type = random.choice(list(self.code_templates.keys()))
        
        # Choose random template for that file type
        template_func = random.choice(self.code_templates[file_type])
        
        # Generate the code
        code_content = template_func()
        
        # Generate unique filename
        filename = self._generate_unique_filename(file_type)
        
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
            'typescript': [
                "type-safe component", "interface definition", "typed utility", "service class",
                "data model", "async handler", "generic function"
            ],
            'dart': [
                "Flutter widget", "data model", "service provider", "utility function",
                "async handler", "custom component", "state manager"
            ],
            'ruby': [
                "gem module", "Rails helper", "utility method", "class definition",
                "DSL builder", "data processor", "API wrapper"
            ],
            'go': [
                "goroutine handler", "struct definition", "package utility", "HTTP handler",
                "concurrent processor", "interface implementation", "middleware"
            ],
            'cpp': [
                "template class", "algorithm implementation", "data structure", "utility function",
                "performance optimizer", "memory manager", "system interface"
            ],
            'c': [
                "system function", "data structure", "memory handler", "utility library",
                "performance function", "low-level interface", "buffer manager"
            ],
            'csharp': [
                ".NET service", "LINQ extension", "async method", "data model",
                "WPF component", "API controller", "utility class"
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
            f"{action} {description}",
            f"{action} {description} for improved functionality",
            f"{action} optimized {description}",
            f"{action} {description} with enhanced features"
        ]
        
        return random.choice(message_formats)
    
    def create_and_commit_file(self):
        """Generate code, create file, and commit to git"""
        try:
            # Generate random code with unique filename
            filename, code_content, file_type = self.generate_random_code()
            
            # Create full file path
            file_path = os.path.join(self.repo_path, filename)
            
            # Check if file exists and create backup if needed
            backup_path = None
            if os.path.exists(file_path):
                backup_path = self._backup_existing_file(filename)
            
            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code_content)
            
            if backup_path:
                print(f"[SUCCESS] Updated file: {filename} (backup created)")
            else:
                print(f"[SUCCESS] Created new file: {filename}")
            
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
                print(f"[SUCCESS] Committed: {commit_message}")
                
                # Push to remote
                subprocess.run(['git', 'push'], check=True)
                print(f"[SUCCESS] Pushed to remote repository")
                
                return True, filename, commit_message
                
            finally:
                os.chdir(original_dir)
                
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Git command failed: {e}")
            return False, None, None
        except Exception as e:
            print(f"[ERROR] Error: {e}")
            return False, None, None
    
    def run_continuous(self, interval_minutes=30, max_commits=None):
        """Run the generator continuously"""
        import time
        
        commit_count = 0
        print(f"[STARTING] Starting random code generator...")
        print(f"[REPO] Repository: {self.repo_path}")
        print(f"[INTERVAL] Interval: {interval_minutes} minutes")
        if max_commits:
            print(f"[TARGET] Max commits: {max_commits}")
        print("=" * 50)
        
        while True:
            try:
                success, filename, commit_message = self.create_and_commit_file()
                
                if success:
                    commit_count += 1
                    print(f"[STATS] Total commits: {commit_count}")
                    
                    if max_commits and commit_count >= max_commits:
                        print(f"[COMPLETE] Reached maximum commits ({max_commits}). Stopping.")
                        break
                else:
                    print("[WARNING] Commit failed, continuing...")
                
                print(f"[WAITING] Waiting {interval_minutes} minutes until next commit...")
                print("=" * 50)
                
                time.sleep(interval_minutes * 60)  # Convert to seconds
                
            except KeyboardInterrupt:
                print("\n[STOPPED] Stopped by user")
                break
            except Exception as e:
                print(f"[ERROR] Unexpected error: {e}")
                print(f"[RETRY] Waiting {interval_minutes} minutes before retry...")
                time.sleep(interval_minutes * 60)

def main():
    """Main function to run the random code generator"""
    
    # Automatic configuration - no user input required
    REPO_PATH = os.getcwd()  # Use current directory
    REMOTE_URL = "https://github.com/jex23/radom_code.git"
    INTERVAL_MINUTES = 5  # Commit every 5 minutes
    MAX_COMMITS = None  # Unlimited commits (set to a number to limit)
    
    print("[STARTING] Automated random code generator...")
    print(f"[REPO] Repository: {REPO_PATH}")
    print(f"[REMOTE] Remote: {REMOTE_URL}")
    print(f"[INTERVAL] Interval: {INTERVAL_MINUTES} minutes")
    
    # Check if it's a git repository, if not, initialize and set remote
    if not os.path.exists(os.path.join(REPO_PATH, '.git')):
        print("[SETUP] Initializing git repository...")
        os.chdir(REPO_PATH)
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'remote', 'add', 'origin', REMOTE_URL], check=True)
        print("[SUCCESS] Git repository initialized and remote added!")
    else:
        print("[SUCCESS] Git repository found!")
    
    # Create generator instance
    generator = RandomCodeGenerator(REPO_PATH)
    
    # Run continuously
    generator.run_continuous(INTERVAL_MINUTES, MAX_COMMITS)

if __name__ == "__main__":
    main()