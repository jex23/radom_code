// Random C header generated on 2025-06-16
#ifndef CHECK_RESULT_H
#define CHECK_RESULT_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 966

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} check_result_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} check_result_item_t;

typedef struct {
    check_result_item_t* items;
    size_t count;
    size_t capacity;
} check_result_collection_t;

// Function declarations
check_result_status_t check_result_init(check_result_collection_t* collection);
check_result_status_t check_result_add_item(check_result_collection_t* collection, 
                                              const check_result_item_t* item);
check_result_status_t check_result_remove_item(check_result_collection_t* collection, 
                                                 int id);
check_result_item_t* check_result_find_item(check_result_collection_t* collection, 
                                              int id);
void check_result_cleanup(check_result_collection_t* collection);

// Utility functions
const char* check_result_status_string(check_result_status_t status);
size_t check_result_get_count(const check_result_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CHECK_RESULT_H
