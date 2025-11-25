// Random C header generated on 2025-11-25
#ifndef UPDATE_VALUE_H
#define UPDATE_VALUE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1668

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} update_value_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} update_value_item_t;

typedef struct {
    update_value_item_t* items;
    size_t count;
    size_t capacity;
} update_value_collection_t;

// Function declarations
update_value_status_t update_value_init(update_value_collection_t* collection);
update_value_status_t update_value_add_item(update_value_collection_t* collection, 
                                              const update_value_item_t* item);
update_value_status_t update_value_remove_item(update_value_collection_t* collection, 
                                                 int id);
update_value_item_t* update_value_find_item(update_value_collection_t* collection, 
                                              int id);
void update_value_cleanup(update_value_collection_t* collection);

// Utility functions
const char* update_value_status_string(update_value_status_t status);
size_t update_value_get_count(const update_value_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // UPDATE_VALUE_H
