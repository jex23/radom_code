// Random C struct generated on 2025-06-03
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} HandleConfig;

HandleConfig* create_handleconfig(const char* name, int value) {
    HandleConfig* obj = malloc(sizeof(HandleConfig));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1343202857;
    
    return obj;
}

void update_handleconfig_value(HandleConfig* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_handleconfig(const HandleConfig* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_handleconfig(HandleConfig* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    HandleConfig* obj = create_handleconfig("sample", 91);
    print_handleconfig(obj);
    free_handleconfig(obj);
    
    return 0;
}
