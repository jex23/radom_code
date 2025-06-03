// Random C header generated on 2025-06-03
#ifndef VALIDATE_VALUE_H
#define VALIDATE_VALUE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 714

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_value_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_value_item_t;

typedef struct {
    validate_value_item_t* items;
    size_t count;
    size_t capacity;
} validate_value_collection_t;

// Function declarations
validate_value_status_t validate_value_init(validate_value_collection_t* collection);
validate_value_status_t validate_value_add_item(validate_value_collection_t* collection, 
                                              const validate_value_item_t* item);
validate_value_status_t validate_value_remove_item(validate_value_collection_t* collection, 
                                                 int id);
validate_value_item_t* validate_value_find_item(validate_value_collection_t* collection, 
                                              int id);
void validate_value_cleanup(validate_value_collection_t* collection);

// Utility functions
const char* validate_value_status_string(validate_value_status_t status);
size_t validate_value_get_count(const validate_value_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_VALUE_H
