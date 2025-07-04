// Random C++ header generated on 2025-07-04
#ifndef GETCONFIG_H
#define GETCONFIG_H

#include <string>
#include <vector>
#include <memory>

namespace utils {

template<typename T>
class GetConfig {
private:
    std::vector<T> data_;
    std::string name_;

public:
    explicit GetConfig(const std::string& name);
    ~GetConfig() = default;
    
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
GetConfig<T>::GetConfig(const std::string& name) : name_(name) {}

template<typename T>
void GetConfig<T>::add(const T& item) {
    data_.push_back(item);
}

template<typename T>
void GetConfig<T>::remove(size_t index) {
    if (index < data_.size()) {
        data_.erase(data_.begin() + index);
    }
}

template<typename T>
T& GetConfig<T>::get(size_t index) {
    return data_.at(index);
}

template<typename T>
const T& GetConfig<T>::get(size_t index) const {
    return data_.at(index);
}

template<typename T>
void GetConfig<T>::clear() {
    data_.clear();
}

} // namespace utils

#endif // GETCONFIG_H
