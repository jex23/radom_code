// Random C struct generated on 2026-01-19
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} GetRequest;

GetRequest* create_getrequest(const char* name, int value) {
    GetRequest* obj = malloc(sizeof(GetRequest));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1074814051;
    
    return obj;
}

void update_getrequest_value(GetRequest* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_getrequest(const GetRequest* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_getrequest(GetRequest* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    GetRequest* obj = create_getrequest("sample", 31);
    print_getrequest(obj);
    free_getrequest(obj);
    
    return 0;
}
