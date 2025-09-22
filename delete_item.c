// Random C header generated on 2025-09-22
#ifndef CREATE_USER_H
#define CREATE_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1422

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} create_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} create_user_item_t;

typedef struct {
    create_user_item_t* items;
    size_t count;
    size_t capacity;
} create_user_collection_t;

// Function declarations
create_user_status_t create_user_init(create_user_collection_t* collection);
create_user_status_t create_user_add_item(create_user_collection_t* collection, 
                                              const create_user_item_t* item);
create_user_status_t create_user_remove_item(create_user_collection_t* collection, 
                                                 int id);
create_user_item_t* create_user_find_item(create_user_collection_t* collection, 
                                              int id);
void create_user_cleanup(create_user_collection_t* collection);

// Utility functions
const char* create_user_status_string(create_user_status_t status);
size_t create_user_get_count(const create_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // CREATE_USER_H
