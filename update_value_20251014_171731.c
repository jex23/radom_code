// Random C struct generated on 2025-10-14
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} SetRequest;

SetRequest* create_setrequest(const char* name, int value) {
    SetRequest* obj = malloc(sizeof(SetRequest));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1912206613;
    
    return obj;
}

void update_setrequest_value(SetRequest* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_setrequest(const SetRequest* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_setrequest(SetRequest* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    SetRequest* obj = create_setrequest("sample", 38);
    print_setrequest(obj);
    free_setrequest(obj);
    
    return 0;
}
