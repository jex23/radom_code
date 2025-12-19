// Random C header generated on 2025-12-19
#ifndef SET_VALUE_H
#define SET_VALUE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1308

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} set_value_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} set_value_item_t;

typedef struct {
    set_value_item_t* items;
    size_t count;
    size_t capacity;
} set_value_collection_t;

// Function declarations
set_value_status_t set_value_init(set_value_collection_t* collection);
set_value_status_t set_value_add_item(set_value_collection_t* collection, 
                                              const set_value_item_t* item);
set_value_status_t set_value_remove_item(set_value_collection_t* collection, 
                                                 int id);
set_value_item_t* set_value_find_item(set_value_collection_t* collection, 
                                              int id);
void set_value_cleanup(set_value_collection_t* collection);

// Utility functions
const char* set_value_status_string(set_value_status_t status);
size_t set_value_get_count(const set_value_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // SET_VALUE_H
