// Random C header generated on 2025-09-16
#ifndef CREATE_RESULT_H
#define CREATE_RESULT_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 973

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} create_result_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} create_result_item_t;

typedef struct {
    create_result_item_t* items;
    size_t count;
    size_t capacity;
} create_result_collection_t;

// Function declarations
create_result_status_t create_result_init(create_result_collection_t* collection);
create_result_status_t create_result_add_item(create_result_collection_t* collection, 
                                              const create_result_item_t* item);
create_result_status_t create_result_remove_item(create_result_collection_t* collection, 
                                                 int id);
create_result_item_t* create_result_find_item(create_result_collection_t* collection, 
                                              int id);
void create_result_cleanup(create_result_collection_t* collection);

// Utility functions
const char* create_result_status_string(create_result_status_t status);
size_t create_result_get_count(const create_result_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CREATE_RESULT_H
