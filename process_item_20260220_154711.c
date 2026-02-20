// Random C header generated on 2026-02-20
#ifndef DELETE_DATA_H
#define DELETE_DATA_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 943

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} delete_data_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} delete_data_item_t;

typedef struct {
    delete_data_item_t* items;
    size_t count;
    size_t capacity;
} delete_data_collection_t;

// Function declarations
delete_data_status_t delete_data_init(delete_data_collection_t* collection);
delete_data_status_t delete_data_add_item(delete_data_collection_t* collection, 
                                              const delete_data_item_t* item);
delete_data_status_t delete_data_remove_item(delete_data_collection_t* collection, 
                                                 int id);
delete_data_item_t* delete_data_find_item(delete_data_collection_t* collection, 
                                              int id);
void delete_data_cleanup(delete_data_collection_t* collection);

// Utility functions
const char* delete_data_status_string(delete_data_status_t status);
size_t delete_data_get_count(const delete_data_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // DELETE_DATA_H
