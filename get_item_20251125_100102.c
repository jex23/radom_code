// Random C struct generated on 2025-11-25
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} DeleteRequest;

DeleteRequest* create_deleterequest(const char* name, int value) {
    DeleteRequest* obj = malloc(sizeof(DeleteRequest));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1391330898;
    
    return obj;
}

void update_deleterequest_value(DeleteRequest* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_deleterequest(const DeleteRequest* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_deleterequest(DeleteRequest* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    DeleteRequest* obj = create_deleterequest("sample", 12);
    print_deleterequest(obj);
    free_deleterequest(obj);
    
    return 0;
}
