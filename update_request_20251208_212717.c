// Random C struct generated on 2025-12-08
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} SetResponse;

SetResponse* create_setresponse(const char* name, int value) {
    SetResponse* obj = malloc(sizeof(SetResponse));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1138311555;
    
    return obj;
}

void update_setresponse_value(SetResponse* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_setresponse(const SetResponse* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_setresponse(SetResponse* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    SetResponse* obj = create_setresponse("sample", 95);
    print_setresponse(obj);
    free_setresponse(obj);
    
    return 0;
}
