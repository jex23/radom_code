// Random C struct generated on 2025-11-27
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} DeleteValue;

DeleteValue* create_deletevalue(const char* name, int value) {
    DeleteValue* obj = malloc(sizeof(DeleteValue));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1453769111;
    
    return obj;
}

void update_deletevalue_value(DeleteValue* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_deletevalue(const DeleteValue* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_deletevalue(DeleteValue* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    DeleteValue* obj = create_deletevalue("sample", 55);
    print_deletevalue(obj);
    free_deletevalue(obj);
    
    return 0;
}
