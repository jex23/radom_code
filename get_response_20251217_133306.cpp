// Random C++ header generated on 2025-12-17
#ifndef HANDLEITEM_H
#define HANDLEITEM_H

#include <string>
#include <vector>
#include <memory>

namespace utils {

template<typename T>
class HandleItem {
private:
    std::vector<T> data_;
    std::string name_;

public:
    explicit HandleItem(const std::string& name);
    ~HandleItem() = default;
    
    void add(const T& item);
    void remove(size_t index);
    T& get(size_t index);
    const T& get(size_t index) const;
    
    size_t size() const { return data_.size(); }
    bool empty() const { return data_.empty(); }
    
    void clear();
    std::string getName() const { return name_; }
};

// Template implementation
template<typename T>
HandleItem<T>::HandleItem(const std::string& name) : name_(name) {}

template<typename T>
void HandleItem<T>::add(const T& item) {
    data_.push_back(item);
}

template<typename T>
void HandleItem<T>::remove(size_t index) {
    if (index < data_.size()) {
        data_.erase(data_.begin() + index);
    }
}

template<typename T>
T& HandleItem<T>::get(size_t index) {
    return data_.at(index);
}

template<typename T>
const T& HandleItem<T>::get(size_t index) const {
    return data_.at(index);
}

template<typename T>
void HandleItem<T>::clear() {
    data_.clear();
}

} // namespace utils

#endif // HANDLEITEM_H
