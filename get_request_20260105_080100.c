// Random C struct generated on 2026-01-05
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} UpdateUser;

UpdateUser* create_updateuser(const char* name, int value) {
    UpdateUser* obj = malloc(sizeof(UpdateUser));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1130734792;
    
    return obj;
}

void update_updateuser_value(UpdateUser* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_updateuser(const UpdateUser* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_updateuser(UpdateUser* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    UpdateUser* obj = create_updateuser("sample", 33);
    print_updateuser(obj);
    free_updateuser(obj);
    
    return 0;
}
