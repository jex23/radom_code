// Random C header generated on 2025-06-12
#ifndef HANDLE_DATA_H
#define HANDLE_DATA_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1733

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} handle_data_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} handle_data_item_t;

typedef struct {
    handle_data_item_t* items;
    size_t count;
    size_t capacity;
} handle_data_collection_t;

// Function declarations
handle_data_status_t handle_data_init(handle_data_collection_t* collection);
handle_data_status_t handle_data_add_item(handle_data_collection_t* collection, 
                                              const handle_data_item_t* item);
handle_data_status_t handle_data_remove_item(handle_data_collection_t* collection, 
                                                 int id);
handle_data_item_t* handle_data_find_item(handle_data_collection_t* collection, 
                                              int id);
void handle_data_cleanup(handle_data_collection_t* collection);

// Utility functions
const char* handle_data_status_string(handle_data_status_t status);
size_t handle_data_get_count(const handle_data_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // HANDLE_DATA_H
