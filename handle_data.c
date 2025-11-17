// Random C header generated on 2025-11-17
#ifndef HANDLE_ITEM_H
#define HANDLE_ITEM_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 2042

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} handle_item_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} handle_item_item_t;

typedef struct {
    handle_item_item_t* items;
    size_t count;
    size_t capacity;
} handle_item_collection_t;

// Function declarations
handle_item_status_t handle_item_init(handle_item_collection_t* collection);
handle_item_status_t handle_item_add_item(handle_item_collection_t* collection, 
                                              const handle_item_item_t* item);
handle_item_status_t handle_item_remove_item(handle_item_collection_t* collection, 
                                                 int id);
handle_item_item_t* handle_item_find_item(handle_item_collection_t* collection, 
                                              int id);
void handle_item_cleanup(handle_item_collection_t* collection);

// Utility functions
const char* handle_item_status_string(handle_item_status_t status);
size_t handle_item_get_count(const handle_item_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // HANDLE_ITEM_H
