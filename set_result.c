// Random C header generated on 2025-08-25
#ifndef CHECK_DATA_H
#define CHECK_DATA_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1639

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} check_data_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} check_data_item_t;

typedef struct {
    check_data_item_t* items;
    size_t count;
    size_t capacity;
} check_data_collection_t;

// Function declarations
check_data_status_t check_data_init(check_data_collection_t* collection);
check_data_status_t check_data_add_item(check_data_collection_t* collection, 
                                              const check_data_item_t* item);
check_data_status_t check_data_remove_item(check_data_collection_t* collection, 
                                                 int id);
check_data_item_t* check_data_find_item(check_data_collection_t* collection, 
                                              int id);
void check_data_cleanup(check_data_collection_t* collection);

// Utility functions
const char* check_data_status_string(check_data_status_t status);
size_t check_data_get_count(const check_data_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CHECK_DATA_H
