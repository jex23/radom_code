// Random C++ class generated on 2025-10-20
#include <iostream>
#include <string>
#include <vector>

class GetData {
private:
    std::string name_;
    int value_;
    std::vector<std::string> history_;

public:
    GetData(const std::string& name, int value = 77) 
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
    GetData obj("sample", 29);
    obj.setValue(88);
    obj.printHistory();
    
    return 0;
}
