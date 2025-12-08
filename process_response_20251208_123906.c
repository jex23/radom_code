// Random C header generated on 2025-12-08
#ifndef GET_REQUEST_H
#define GET_REQUEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 974

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} get_request_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} get_request_item_t;

typedef struct {
    get_request_item_t* items;
    size_t count;
    size_t capacity;
} get_request_collection_t;

// Function declarations
get_request_status_t get_request_init(get_request_collection_t* collection);
get_request_status_t get_request_add_item(get_request_collection_t* collection, 
                                              const get_request_item_t* item);
get_request_status_t get_request_remove_item(get_request_collection_t* collection, 
                                                 int id);
get_request_item_t* get_request_find_item(get_request_collection_t* collection, 
                                              int id);
void get_request_cleanup(get_request_collection_t* collection);

// Utility functions
const char* get_request_status_string(get_request_status_t status);
size_t get_request_get_count(const get_request_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // GET_REQUEST_H
