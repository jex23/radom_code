// Random C header generated on 2025-07-23
#ifndef HANDLE_VALUE_H
#define HANDLE_VALUE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1314

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} handle_value_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} handle_value_item_t;

typedef struct {
    handle_value_item_t* items;
    size_t count;
    size_t capacity;
} handle_value_collection_t;

// Function declarations
handle_value_status_t handle_value_init(handle_value_collection_t* collection);
handle_value_status_t handle_value_add_item(handle_value_collection_t* collection, 
                                              const handle_value_item_t* item);
handle_value_status_t handle_value_remove_item(handle_value_collection_t* collection, 
                                                 int id);
handle_value_item_t* handle_value_find_item(handle_value_collection_t* collection, 
                                              int id);
void handle_value_cleanup(handle_value_collection_t* collection);

// Utility functions
const char* handle_value_status_string(handle_value_status_t status);
size_t handle_value_get_count(const handle_value_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // HANDLE_VALUE_H
