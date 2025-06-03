// Random TypeScript function generated on 2025-06-03

interface DeleteItem {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function set_result(value_hpb: DeleteItem[]): DeleteItem[] {
    const multiplier: number = 8;
    
    return value_hpb
        .filter((item: DeleteItem) => item.active)
        .map((item: DeleteItem, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: DeleteItem[] = [
    { id: 1, name: "Item1", value: 14, active: true },
    { id: 2, name: "Item2", value: 37, active: false }
];

const result = set_result(testData);
console.log('Processed items:', result);

export { set_result, DeleteItem };
