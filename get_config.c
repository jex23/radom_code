// Random C header generated on 2025-06-05
#ifndef CHECK_REQUEST_H
#define CHECK_REQUEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1847

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} check_request_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} check_request_item_t;

typedef struct {
    check_request_item_t* items;
    size_t count;
    size_t capacity;
} check_request_collection_t;

// Function declarations
check_request_status_t check_request_init(check_request_collection_t* collection);
check_request_status_t check_request_add_item(check_request_collection_t* collection, 
                                              const check_request_item_t* item);
check_request_status_t check_request_remove_item(check_request_collection_t* collection, 
                                                 int id);
check_request_item_t* check_request_find_item(check_request_collection_t* collection, 
                                              int id);
void check_request_cleanup(check_request_collection_t* collection);

// Utility functions
const char* check_request_status_string(check_request_status_t status);
size_t check_request_get_count(const check_request_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CHECK_REQUEST_H
