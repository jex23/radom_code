// Random C header generated on 2025-12-29
#ifndef VALIDATE_CONFIG_H
#define VALIDATE_CONFIG_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_NAME_LENGTH 256
#define DEFAULT_BUFFER_SIZE 620

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_PARAM = -2,
    STATUS_OUT_OF_MEMORY = -3
} validate_config_status_t;

typedef struct {
    char name[MAX_NAME_LENGTH];
    int id;
    double value;
    size_t size;
} validate_config_item_t;

typedef struct {
    validate_config_item_t* items;
    size_t count;
    size_t capacity;
} validate_config_collection_t;

// Function declarations
validate_config_status_t validate_config_init(validate_config_collection_t* collection);
validate_config_status_t validate_config_add_item(validate_config_collection_t* collection, 
                                              const validate_config_item_t* item);
validate_config_status_t validate_config_remove_item(validate_config_collection_t* collection, 
                                                 int id);
validate_config_item_t* validate_config_find_item(validate_config_collection_t* collection, 
                                              int id);
void validate_config_cleanup(validate_config_collection_t* collection);

// Utility functions
const char* validate_config_status_string(validate_config_status_t status);
size_t validate_config_get_count(const validate_config_collection_t* collection);

#ifdef __cplusplus
}
#endif

#endif // VALIDATE_CONFIG_H
