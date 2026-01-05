// Random C struct generated on 2026-01-05
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} CreateValue;

CreateValue* create_createvalue(const char* name, int value) {
    CreateValue* obj = malloc(sizeof(CreateValue));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1862145967;
    
    return obj;
}

void update_createvalue_value(CreateValue* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_createvalue(const CreateValue* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_createvalue(CreateValue* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    CreateValue* obj = create_createvalue("sample", 62);
    print_createvalue(obj);
    free_createvalue(obj);
    
    return 0;
}
