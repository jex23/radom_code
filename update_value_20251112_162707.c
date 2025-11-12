// Random C struct generated on 2025-11-12
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} CreateItem;

CreateItem* create_createitem(const char* name, int value) {
    CreateItem* obj = malloc(sizeof(CreateItem));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1532180364;
    
    return obj;
}

void update_createitem_value(CreateItem* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_createitem(const CreateItem* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_createitem(CreateItem* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    CreateItem* obj = create_createitem("sample", 32);
    print_createitem(obj);
    free_createitem(obj);
    
    return 0;
}
