// Random C header generated on 2025-08-20
#ifndef CHECK_VALUE_H
#define CHECK_VALUE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1402

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} check_value_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} check_value_item_t;

typedef struct {
    check_value_item_t* items;
    size_t count;
    size_t capacity;
} check_value_collection_t;

// Function declarations
check_value_status_t check_value_init(check_value_collection_t* collection);
check_value_status_t check_value_add_item(check_value_collection_t* collection, 
                                              const check_value_item_t* item);
check_value_status_t check_value_remove_item(check_value_collection_t* collection, 
                                                 int id);
check_value_item_t* check_value_find_item(check_value_collection_t* collection, 
                                              int id);
void check_value_cleanup(check_value_collection_t* collection);

// Utility functions
const char* check_value_status_string(check_value_status_t status);
size_t check_value_get_count(const check_value_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CHECK_VALUE_H
