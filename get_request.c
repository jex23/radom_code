// Random C struct generated on 2025-10-08
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} CreateUser;

CreateUser* create_createuser(const char* name, int value) {
    CreateUser* obj = malloc(sizeof(CreateUser));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1434609003;
    
    return obj;
}

void update_createuser_value(CreateUser* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_createuser(const CreateUser* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_createuser(CreateUser* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    CreateUser* obj = create_createuser("sample", 82);
    print_createuser(obj);
    free_createuser(obj);
    
    return 0;
}
