// Random C header generated on 2025-09-19
#ifndef GET_RESPONSE_H
#define GET_RESPONSE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 992

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} get_response_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} get_response_item_t;

typedef struct {
    get_response_item_t* items;
    size_t count;
    size_t capacity;
} get_response_collection_t;

// Function declarations
get_response_status_t get_response_init(get_response_collection_t* collection);
get_response_status_t get_response_add_item(get_response_collection_t* collection, 
                                              const get_response_item_t* item);
get_response_status_t get_response_remove_item(get_response_collection_t* collection, 
                                                 int id);
get_response_item_t* get_response_find_item(get_response_collection_t* collection, 
                                              int id);
void get_response_cleanup(get_response_collection_t* collection);

// Utility functions
const char* get_response_status_string(get_response_status_t status);
size_t get_response_get_count(const get_response_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // GET_RESPONSE_H
