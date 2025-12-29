// Random C++ header generated on 2025-12-29
#ifndef CREATECONFIG_H
#define CREATECONFIG_H

#include <string>
#include <vector>
#include <memory>

namespace utils {

template<typename T>
class CreateConfig {
private:
    std::vector<T> data_;
    std::string name_;

public:
    explicit CreateConfig(const std::string& name);
    ~CreateConfig() = default;
    
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
CreateConfig<T>::CreateConfig(const std::string& name) : name_(name) {}

template<typename T>
void CreateConfig<T>::add(const T& item) {
    data_.push_back(item);
}

template<typename T>
void CreateConfig<T>::remove(size_t index) {
    if (index < data_.size()) {
        data_.erase(data_.begin() + index);
    }
}

template<typename T>
T& CreateConfig<T>::get(size_t index) {
    return data_.at(index);
}

template<typename T>
const T& CreateConfig<T>::get(size_t index) const {
    return data_.at(index);
}

template<typename T>
void CreateConfig<T>::clear() {
    data_.clear();
}

} // namespace utils

#endif // CREATECONFIG_H
