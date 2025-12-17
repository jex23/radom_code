// Random C header generated on 2025-12-17
#ifndef SET_USER_H
#define SET_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1673

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} set_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} set_user_item_t;

typedef struct {
    set_user_item_t* items;
    size_t count;
    size_t capacity;
} set_user_collection_t;

// Function declarations
set_user_status_t set_user_init(set_user_collection_t* collection);
set_user_status_t set_user_add_item(set_user_collection_t* collection, 
                                              const set_user_item_t* item);
set_user_status_t set_user_remove_item(set_user_collection_t* collection, 
                                                 int id);
set_user_item_t* set_user_find_item(set_user_collection_t* collection, 
                                              int id);
void set_user_cleanup(set_user_collection_t* collection);

// Utility functions
const char* set_user_status_string(set_user_status_t status);
size_t set_user_get_count(const set_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // SET_USER_H
