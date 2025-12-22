// Random TypeScript function generated on 2025-12-22

interface DeleteItem {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_data(config_wyj: DeleteItem[]): DeleteItem[] {
    const multiplier: number = 3;
    
    return config_wyj
        .filter((item: DeleteItem) => item.active)
        .map((item: DeleteItem, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: DeleteItem[] = [
    { id: 1, name: "Item1", value: 91, active: true },
    { id: 2, name: "Item2", value: 36, active: false }
];

const result = update_data(testData);
console.log('Processed items:', result);

export { update_data, DeleteItem };
