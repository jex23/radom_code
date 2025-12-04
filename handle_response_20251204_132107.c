// Random C header generated on 2025-12-04
#ifndef PROCESS_RESULT_H
#define PROCESS_RESULT_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1483

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} process_result_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} process_result_item_t;

typedef struct {
    process_result_item_t* items;
    size_t count;
    size_t capacity;
} process_result_collection_t;

// Function declarations
process_result_status_t process_result_init(process_result_collection_t* collection);
process_result_status_t process_result_add_item(process_result_collection_t* collection, 
                                              const process_result_item_t* item);
process_result_status_t process_result_remove_item(process_result_collection_t* collection, 
                                                 int id);
process_result_item_t* process_result_find_item(process_result_collection_t* collection, 
                                              int id);
void process_result_cleanup(process_result_collection_t* collection);

// Utility functions
const char* process_result_status_string(process_result_status_t status);
size_t process_result_get_count(const process_result_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // PROCESS_RESULT_H
