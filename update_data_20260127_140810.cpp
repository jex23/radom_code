// Random C++ class generated on 2026-01-27
#include <iostream>
#include <string>
#include <vector>

class GetItem {
private:
    std::string name_;
    int value_;
    std::vector<std::string> history_;

public:
    GetItem(const std::string& name, int value = 97) 
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
    GetItem obj("sample", 11);
    obj.setValue(80);
    obj.printHistory();
    
    return 0;
}
