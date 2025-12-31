// Random C header generated on 2025-12-31
#ifndef VALIDATE_USER_H
#define VALIDATE_USER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 2035

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_user_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_user_item_t;

typedef struct {
    validate_user_item_t* items;
    size_t count;
    size_t capacity;
} validate_user_collection_t;

// Function declarations
validate_user_status_t validate_user_init(validate_user_collection_t* collection);
validate_user_status_t validate_user_add_item(validate_user_collection_t* collection, 
                                              const validate_user_item_t* item);
validate_user_status_t validate_user_remove_item(validate_user_collection_t* collection, 
                                                 int id);
validate_user_item_t* validate_user_find_item(validate_user_collection_t* collection, 
                                              int id);
void validate_user_cleanup(validate_user_collection_t* collection);

// Utility functions
const char* validate_user_status_string(validate_user_status_t status);
size_t validate_user_get_count(const validate_user_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_USER_H
