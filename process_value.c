// Random C function generated on 2025-07-23
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    char name[50];
    double value;
} Item;

Item* get_item(const Item* items, int count, int* result_count) {
    const double multiplier = 10.0;
    Item* result = malloc(count * sizeof(Item));
    
    if (result == NULL) {
        *result_count = 0;
        return NULL;
    }
    
    for (int i = 0; i < count; i++) {
        result[i].id = items[i].id;
        snprintf(result[i].name, sizeof(result[i].name), "%s_processed", items[i].name);
        result[i].value = items[i].value * multiplier;
    }
    
    *result_count = count;
    return result;
}

int main() {
    Item testData[] = {
        {1, "item1", 29.0},
        {2, "item2", 42.0}
    };
    
    int result_count;
    Item* result = get_item(testData, 2, &result_count);
    
    printf("Processed %d items\n", result_count);
    
    if (result) {
        free(result);
    }
    
    return 0;
}
