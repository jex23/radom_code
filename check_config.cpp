// Random C++ function generated on 2025-06-19
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

struct Item {
    int id;
    std::string name;
    double value;
    
    Item(int id, const std::string& name, double value) 
        : id(id), name(name), value(value) {}
};

std::vector<Item> create_data(const std::vector<Item>& items) {
    const double multiplier = 5.0;
    std::vector<Item> result;
    
    std::transform(items.begin(), items.end(), std::back_inserter(result),
        [multiplier](const Item& item) {
            return Item(item.id, item.name + "_processed", item.value * multiplier);
        });
    
    return result;
}

int main() {
    std::vector<Item> testData = {
        Item(1, "item1", 47.0),
        Item(2, "item2", 65.0)
    };
    
    auto result = create_data(testData);
    std::cout << "Processed " << result.size() << " items" << std::endl;
    
    return 0;
}
