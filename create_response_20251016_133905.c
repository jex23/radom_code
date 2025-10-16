// Random C header generated on 2025-10-16
#ifndef CREATE_ITEM_H
#define CREATE_ITEM_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1545

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} create_item_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} create_item_item_t;

typedef struct {
    create_item_item_t* items;
    size_t count;
    size_t capacity;
} create_item_collection_t;

// Function declarations
create_item_status_t create_item_init(create_item_collection_t* collection);
create_item_status_t create_item_add_item(create_item_collection_t* collection, 
                                              const create_item_item_t* item);
create_item_status_t create_item_remove_item(create_item_collection_t* collection, 
                                                 int id);
create_item_item_t* create_item_find_item(create_item_collection_t* collection, 
                                              int id);
void create_item_cleanup(create_item_collection_t* collection);

// Utility functions
const char* create_item_status_string(create_item_status_t status);
size_t create_item_get_count(const create_item_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CREATE_ITEM_H
