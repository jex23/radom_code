// Random C header generated on 2025-11-06
#ifndef PROCESS_RESPONSE_H
#define PROCESS_RESPONSE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1188

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} process_response_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} process_response_item_t;

typedef struct {
    process_response_item_t* items;
    size_t count;
    size_t capacity;
} process_response_collection_t;

// Function declarations
process_response_status_t process_response_init(process_response_collection_t* collection);
process_response_status_t process_response_add_item(process_response_collection_t* collection, 
                                              const process_response_item_t* item);
process_response_status_t process_response_remove_item(process_response_collection_t* collection, 
                                                 int id);
process_response_item_t* process_response_find_item(process_response_collection_t* collection, 
                                              int id);
void process_response_cleanup(process_response_collection_t* collection);

// Utility functions
const char* process_response_status_string(process_response_status_t status);
size_t process_response_get_count(const process_response_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // PROCESS_RESPONSE_H
