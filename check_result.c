// Random C header generated on 2025-08-01
#ifndef PROCESS_USER_H
#define PROCESS_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1075

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} process_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} process_user_item_t;

typedef struct {
    process_user_item_t* items;
    size_t count;
    size_t capacity;
} process_user_collection_t;

// Function declarations
process_user_status_t process_user_init(process_user_collection_t* collection);
process_user_status_t process_user_add_item(process_user_collection_t* collection, 
                                              const process_user_item_t* item);
process_user_status_t process_user_remove_item(process_user_collection_t* collection, 
                                                 int id);
process_user_item_t* process_user_find_item(process_user_collection_t* collection, 
                                              int id);
void process_user_cleanup(process_user_collection_t* collection);

// Utility functions
const char* process_user_status_string(process_user_status_t status);
size_t process_user_get_count(const process_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // PROCESS_USER_H
