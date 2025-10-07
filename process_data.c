// Random C header generated on 2025-10-07
#ifndef SET_REQUEST_H
#define SET_REQUEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1724

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} set_request_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} set_request_item_t;

typedef struct {
    set_request_item_t* items;
    size_t count;
    size_t capacity;
} set_request_collection_t;

// Function declarations
set_request_status_t set_request_init(set_request_collection_t* collection);
set_request_status_t set_request_add_item(set_request_collection_t* collection, 
                                              const set_request_item_t* item);
set_request_status_t set_request_remove_item(set_request_collection_t* collection, 
                                                 int id);
set_request_item_t* set_request_find_item(set_request_collection_t* collection, 
                                              int id);
void set_request_cleanup(set_request_collection_t* collection);

// Utility functions
const char* set_request_status_string(set_request_status_t status);
size_t set_request_get_count(const set_request_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // SET_REQUEST_H
