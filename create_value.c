// Random C struct generated on 2025-10-13
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int value;
    int active;
    long timestamp;
} GetData;

GetData* create_getdata(const char* name, int value) {
    GetData* obj = malloc(sizeof(GetData));
    if (obj == NULL) return NULL;
    
    strncpy(obj->name, name, sizeof(obj->name) - 1);
    obj->name[sizeof(obj->name) - 1] = '\0';
    obj->value = value;
    obj->active = 1;
    obj->timestamp = 1583225088;
    
    return obj;
}

void update_getdata_value(GetData* obj, int new_value) {
    if (obj != NULL) {
        obj->value = new_value;
    }
}

void print_getdata(const GetData* obj) {
    if (obj != NULL) {
        printf("Name: %s, Value: %d, Active: %d\n", 
               obj->name, obj->value, obj->active);
    }
}

void free_getdata(GetData* obj) {
    if (obj != NULL) {
        free(obj);
    }
}

int main() {
    GetData* obj = create_getdata("sample", 54);
    print_getdata(obj);
    free_getdata(obj);
    
    return 0;
}
