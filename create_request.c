// Random C struct generated on 2025-08-27
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} HandleRequest;

HandleRequest* create_handlerequest(const char* name, int value) {
    HandleRequest* obj = malloc(sizeof(HandleRequest));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1644660562;
    
    return obj;
}

void update_handlerequest_value(HandleRequest* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_handlerequest(const HandleRequest* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_handlerequest(HandleRequest* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    HandleRequest* obj = create_handlerequest("sample", 21);
    print_handlerequest(obj);
    free_handlerequest(obj);
    
    return 0;
}
