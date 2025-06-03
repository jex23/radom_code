// Random C header generated on 2025-06-03
#ifndef VALIDATE_REQUEST_H
#define VALIDATE_REQUEST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1013

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_request_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_request_item_t;

typedef struct {
    validate_request_item_t* items;
    size_t count;
    size_t capacity;
} validate_request_collection_t;

// Function declarations
validate_request_status_t validate_request_init(validate_request_collection_t* collection);
validate_request_status_t validate_request_add_item(validate_request_collection_t* collection, 
                                              const validate_request_item_t* item);
validate_request_status_t validate_request_remove_item(validate_request_collection_t* collection, 
                                                 int id);
validate_request_item_t* validate_request_find_item(validate_request_collection_t* collection, 
                                              int id);
void validate_request_cleanup(validate_request_collection_t* collection);

// Utility functions
const char* validate_request_status_string(validate_request_status_t status);
size_t validate_request_get_count(const validate_request_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_REQUEST_H
