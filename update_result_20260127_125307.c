// Random C header generated on 2026-01-27
#ifndef HANDLE_USER_H
#define HANDLE_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1565

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} handle_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} handle_user_item_t;

typedef struct {
    handle_user_item_t* items;
    size_t count;
    size_t capacity;
} handle_user_collection_t;

// Function declarations
handle_user_status_t handle_user_init(handle_user_collection_t* collection);
handle_user_status_t handle_user_add_item(handle_user_collection_t* collection, 
                                              const handle_user_item_t* item);
handle_user_status_t handle_user_remove_item(handle_user_collection_t* collection, 
                                                 int id);
handle_user_item_t* handle_user_find_item(handle_user_collection_t* collection, 
                                              int id);
void handle_user_cleanup(handle_user_collection_t* collection);

// Utility functions
const char* handle_user_status_string(handle_user_status_t status);
size_t handle_user_get_count(const handle_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // HANDLE_USER_H
