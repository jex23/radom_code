// Random C header generated on 2025-08-13
#ifndef UPDATE_USER_H
#define UPDATE_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1287

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} update_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} update_user_item_t;

typedef struct {
    update_user_item_t* items;
    size_t count;
    size_t capacity;
} update_user_collection_t;

// Function declarations
update_user_status_t update_user_init(update_user_collection_t* collection);
update_user_status_t update_user_add_item(update_user_collection_t* collection, 
                                              const update_user_item_t* item);
update_user_status_t update_user_remove_item(update_user_collection_t* collection, 
                                                 int id);
update_user_item_t* update_user_find_item(update_user_collection_t* collection, 
                                              int id);
void update_user_cleanup(update_user_collection_t* collection);

// Utility functions
const char* update_user_status_string(update_user_status_t status);
size_t update_user_get_count(const update_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // UPDATE_USER_H
