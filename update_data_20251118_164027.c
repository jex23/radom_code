// Random C header generated on 2025-11-18
#ifndef DELETE_USER_H
#define DELETE_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 861

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} delete_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} delete_user_item_t;

typedef struct {
    delete_user_item_t* items;
    size_t count;
    size_t capacity;
} delete_user_collection_t;

// Function declarations
delete_user_status_t delete_user_init(delete_user_collection_t* collection);
delete_user_status_t delete_user_add_item(delete_user_collection_t* collection, 
                                              const delete_user_item_t* item);
delete_user_status_t delete_user_remove_item(delete_user_collection_t* collection, 
                                                 int id);
delete_user_item_t* delete_user_find_item(delete_user_collection_t* collection, 
                                              int id);
void delete_user_cleanup(delete_user_collection_t* collection);

// Utility functions
const char* delete_user_status_string(delete_user_status_t status);
size_t delete_user_get_count(const delete_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // DELETE_USER_H
