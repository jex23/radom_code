// Random C struct generated on 2025-09-26
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} HandleResult;

HandleResult* create_handleresult(const char* name, int value) {
    HandleResult* obj = malloc(sizeof(HandleResult));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1227457048;
    
    return obj;
}

void update_handleresult_value(HandleResult* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_handleresult(const HandleResult* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_handleresult(HandleResult* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    HandleResult* obj = create_handleresult("sample", 67);
    print_handleresult(obj);
    free_handleresult(obj);
    
    return 0;
}
