// Random C++ class generated on 2025-07-16
#include <iostream>
#include <string>
#include <vector>

class ProcessResult {
private:
    std::string name_;
    int value_;
    std::vector<std::string> history_;

public:
    ProcessResult(const std::string& name, int value = 100) 
        : name_(name), value_(value) {}
    
    void setName(const std::string& name) {
        history_.push_back("Name changed from " + name_ + " to " + name);
        name_ = name;
    }
    
    void setValue(int value) {
        history_.push_back("Value changed from " + std::to_string(value_) + " to " + std::to_string(value));
        value_ = value;
    }
    
    std::string getName() const { return name_; }
    int getValue() const { return value_; }
    
    void printHistory() const {
        for (const auto& entry : history_) {
            std::cout << entry << std::endl;
        }
    }
};

int main() {
    ProcessResult obj("sample", 38);
    obj.setValue(93);
    obj.printHistory();
    
    return 0;
}
