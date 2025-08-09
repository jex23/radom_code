// Random C header generated on 2025-08-09
#ifndef VALIDATE_ITEM_H
#define VALIDATE_ITEM_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1977

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_item_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_item_item_t;

typedef struct {
    validate_item_item_t* items;
    size_t count;
    size_t capacity;
} validate_item_collection_t;

// Function declarations
validate_item_status_t validate_item_init(validate_item_collection_t* collection);
validate_item_status_t validate_item_add_item(validate_item_collection_t* collection, 
                                              const validate_item_item_t* item);
validate_item_status_t validate_item_remove_item(validate_item_collection_t* collection, 
                                                 int id);
validate_item_item_t* validate_item_find_item(validate_item_collection_t* collection, 
                                              int id);
void validate_item_cleanup(validate_item_collection_t* collection);

// Utility functions
const char* validate_item_status_string(validate_item_status_t status);
size_t validate_item_get_count(const validate_item_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_ITEM_H
