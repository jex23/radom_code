// Random C header generated on 2025-10-25
#ifndef VALIDATE_DATA_H
#define VALIDATE_DATA_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1664

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_data_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_data_item_t;

typedef struct {
    validate_data_item_t* items;
    size_t count;
    size_t capacity;
} validate_data_collection_t;

// Function declarations
validate_data_status_t validate_data_init(validate_data_collection_t* collection);
validate_data_status_t validate_data_add_item(validate_data_collection_t* collection, 
                                              const validate_data_item_t* item);
validate_data_status_t validate_data_remove_item(validate_data_collection_t* collection, 
                                                 int id);
validate_data_item_t* validate_data_find_item(validate_data_collection_t* collection, 
                                              int id);
void validate_data_cleanup(validate_data_collection_t* collection);

// Utility functions
const char* validate_data_status_string(validate_data_status_t status);
size_t validate_data_get_count(const validate_data_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_DATA_H
