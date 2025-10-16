// Random C header generated on 2025-10-16
#ifndef PROCESS_ITEM_H
#define PROCESS_ITEM_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 866

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} process_item_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} process_item_item_t;

typedef struct {
    process_item_item_t* items;
    size_t count;
    size_t capacity;
} process_item_collection_t;

// Function declarations
process_item_status_t process_item_init(process_item_collection_t* collection);
process_item_status_t process_item_add_item(process_item_collection_t* collection, 
                                              const process_item_item_t* item);
process_item_status_t process_item_remove_item(process_item_collection_t* collection, 
                                                 int id);
process_item_item_t* process_item_find_item(process_item_collection_t* collection, 
                                              int id);
void process_item_cleanup(process_item_collection_t* collection);

// Utility functions
const char* process_item_status_string(process_item_status_t status);
size_t process_item_get_count(const process_item_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // PROCESS_ITEM_H
