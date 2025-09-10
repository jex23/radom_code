// Random C header generated on 2025-09-10
#ifndef UPDATE_RESPONSE_H
#define UPDATE_RESPONSE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 1485

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} update_response_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} update_response_item_t;

typedef struct {
    update_response_item_t* items;
    size_t count;
    size_t capacity;
} update_response_collection_t;

// Function declarations
update_response_status_t update_response_init(update_response_collection_t* collection);
update_response_status_t update_response_add_item(update_response_collection_t* collection, 
                                              const update_response_item_t* item);
update_response_status_t update_response_remove_item(update_response_collection_t* collection, 
                                                 int id);
update_response_item_t* update_response_find_item(update_response_collection_t* collection, 
                                              int id);
void update_response_cleanup(update_response_collection_t* collection);

// Utility functions
const char* update_response_status_string(update_response_status_t status);
size_t update_response_get_count(const update_response_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // UPDATE_RESPONSE_H
