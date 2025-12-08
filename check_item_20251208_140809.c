// Random C struct generated on 2025-12-08
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} UpdateResponse;

UpdateResponse* create_updateresponse(const char* name, int value) {
    UpdateResponse* obj = malloc(sizeof(UpdateResponse));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1440180440;
    
    return obj;
}

void update_updateresponse_value(UpdateResponse* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_updateresponse(const UpdateResponse* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_updateresponse(UpdateResponse* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    UpdateResponse* obj = create_updateresponse("sample", 78);
    print_updateresponse(obj);
    free_updateresponse(obj);
    
    return 0;
}
