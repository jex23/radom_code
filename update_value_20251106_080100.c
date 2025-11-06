// Random C struct generated on 2025-11-06
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} CreateResponse;

CreateResponse* create_createresponse(const char* name, int value) {
    CreateResponse* obj = malloc(sizeof(CreateResponse));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1213257187;
    
    return obj;
}

void update_createresponse_value(CreateResponse* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_createresponse(const CreateResponse* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_createresponse(CreateResponse* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    CreateResponse* obj = create_createresponse("sample", 52);
    print_createresponse(obj);
    free_createresponse(obj);
    
    return 0;
}
