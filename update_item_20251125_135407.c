// Random C header generated on 2025-11-25
#ifndef CHECK_USER_H
#define CHECK_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1490

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} check_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} check_user_item_t;

typedef struct {
    check_user_item_t* items;
    size_t count;
    size_t capacity;
} check_user_collection_t;

// Function declarations
check_user_status_t check_user_init(check_user_collection_t* collection);
check_user_status_t check_user_add_item(check_user_collection_t* collection, 
                                              const check_user_item_t* item);
check_user_status_t check_user_remove_item(check_user_collection_t* collection, 
                                                 int id);
check_user_item_t* check_user_find_item(check_user_collection_t* collection, 
                                              int id);
void check_user_cleanup(check_user_collection_t* collection);

// Utility functions
const char* check_user_status_string(check_user_status_t status);
size_t check_user_get_count(const check_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CHECK_USER_H
