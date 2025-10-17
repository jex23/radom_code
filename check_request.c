// Random C struct generated on 2025-10-17
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} HandleValue;

HandleValue* create_handlevalue(const char* name, int value) {
    HandleValue* obj = malloc(sizeof(HandleValue));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1156015283;
    
    return obj;
}

void update_handlevalue_value(HandleValue* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_handlevalue(const HandleValue* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_handlevalue(HandleValue* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    HandleValue* obj = create_handlevalue("sample", 46);
    print_handlevalue(obj);
    free_handlevalue(obj);
    
    return 0;
}
