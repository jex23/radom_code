// Random C++ class generated on 2025-07-22
#include <iostream>
#include <string>
#include <vector>

class SetItem {
private:
    std::string name_;
    int value_;
    std::vector<std::string> history_;

public:
    SetItem(const std::string& name, int value = 16) 
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
    SetItem obj("sample", 19);
    obj.setValue(99);
    obj.printHistory();
    
    return 0;
}
