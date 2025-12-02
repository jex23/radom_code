// Random C header generated on 2025-12-02
#ifndef CREATE_RESPONSE_H
#define CREATE_RESPONSE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1148

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} create_response_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} create_response_item_t;

typedef struct {
    create_response_item_t* items;
    size_t count;
    size_t capacity;
} create_response_collection_t;

// Function declarations
create_response_status_t create_response_init(create_response_collection_t* collection);
create_response_status_t create_response_add_item(create_response_collection_t* collection, 
                                              const create_response_item_t* item);
create_response_status_t create_response_remove_item(create_response_collection_t* collection, 
                                                 int id);
create_response_item_t* create_response_find_item(create_response_collection_t* collection, 
                                              int id);
void create_response_cleanup(create_response_collection_t* collection);

// Utility functions
const char* create_response_status_string(create_response_status_t status);
size_t create_response_get_count(const create_response_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CREATE_RESPONSE_H
