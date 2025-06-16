// Random C++ header generated on 2025-06-16
#ifndef VALIDATERESULT_H
#define VALIDATERESULT_H

#include <string>
#include <vector>
#include <memory>

namespace utils {

template<typename T>
class ValidateResult {
private:
    std::vector<T> data_;
    std::string name_;

public:
    explicit ValidateResult(const std::string& name);
    ~ValidateResult() = default;
    
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
ValidateResult<T>::ValidateResult(const std::string& name) : name_(name) {}

template<typename T>
void ValidateResult<T>::add(const T& item) {
    data_.push_back(item);
}

template<typename T>
void ValidateResult<T>::remove(size_t index) {
    if (index < data_.size()) {
        data_.erase(data_.begin() + index);
    }
}

template<typename T>
T& ValidateResult<T>::get(size_t index) {
    return data_.at(index);
}

template<typename T>
const T& ValidateResult<T>::get(size_t index) const {
    return data_.at(index);
}

template<typename T>
void ValidateResult<T>::clear() {
    data_.clear();
}

} // namespace utils

#endif // VALIDATERESULT_H
