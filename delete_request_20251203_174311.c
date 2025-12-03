// Random C header generated on 2025-12-03
#ifndef VALIDATE_RESPONSE_H
#define VALIDATE_RESPONSE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 584

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_response_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_response_item_t;

typedef struct {
    validate_response_item_t* items;
    size_t count;
    size_t capacity;
} validate_response_collection_t;

// Function declarations
validate_response_status_t validate_response_init(validate_response_collection_t* collection);
validate_response_status_t validate_response_add_item(validate_response_collection_t* collection, 
                                              const validate_response_item_t* item);
validate_response_status_t validate_response_remove_item(validate_response_collection_t* collection, 
                                                 int id);
validate_response_item_t* validate_response_find_item(validate_response_collection_t* collection, 
                                              int id);
void validate_response_cleanup(validate_response_collection_t* collection);

// Utility functions
const char* validate_response_status_string(validate_response_status_t status);
size_t validate_response_get_count(const validate_response_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_RESPONSE_H
