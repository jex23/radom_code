// Random C header generated on 2026-01-22
#ifndef DELETE_REQUEST_H
#define DELETE_REQUEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1551

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} delete_request_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} delete_request_item_t;

typedef struct {
    delete_request_item_t* items;
    size_t count;
    size_t capacity;
} delete_request_collection_t;

// Function declarations
delete_request_status_t delete_request_init(delete_request_collection_t* collection);
delete_request_status_t delete_request_add_item(delete_request_collection_t* collection, 
                                              const delete_request_item_t* item);
delete_request_status_t delete_request_remove_item(delete_request_collection_t* collection, 
                                                 int id);
delete_request_item_t* delete_request_find_item(delete_request_collection_t* collection, 
                                              int id);
void delete_request_cleanup(delete_request_collection_t* collection);

// Utility functions
const char* delete_request_status_string(delete_request_status_t status);
size_t delete_request_get_count(const delete_request_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // DELETE_REQUEST_H
