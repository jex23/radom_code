// Random C header generated on 2025-12-20
#ifndef CHECK_RESPONSE_H
#define CHECK_RESPONSE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 683

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} check_response_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} check_response_item_t;

typedef struct {
    check_response_item_t* items;
    size_t count;
    size_t capacity;
} check_response_collection_t;

// Function declarations
check_response_status_t check_response_init(check_response_collection_t* collection);
check_response_status_t check_response_add_item(check_response_collection_t* collection, 
                                              const check_response_item_t* item);
check_response_status_t check_response_remove_item(check_response_collection_t* collection, 
                                                 int id);
check_response_item_t* check_response_find_item(check_response_collection_t* collection, 
                                              int id);
void check_response_cleanup(check_response_collection_t* collection);

// Utility functions
const char* check_response_status_string(check_response_status_t status);
size_t check_response_get_count(const check_response_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CHECK_RESPONSE_H
