// Random C struct generated on 2026-03-05
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} ProcessResponse;

ProcessResponse* create_processresponse(const char* name, int value) {
    ProcessResponse* obj = malloc(sizeof(ProcessResponse));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1567761641;
    
    return obj;
}

void update_processresponse_value(ProcessResponse* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_processresponse(const ProcessResponse* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_processresponse(ProcessResponse* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    ProcessResponse* obj = create_processresponse("sample", 72);
    print_processresponse(obj);
    free_processresponse(obj);
    
    return 0;
}
