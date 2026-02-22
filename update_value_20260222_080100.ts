// Random TypeScript function generated on 2026-02-22

interface HandleUser {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function get_result(item_him: HandleUser[]): HandleUser[] {
    const multiplier: number = 7;
    
    return item_him
        .filter((item: HandleUser) => item.active)
        .map((item: HandleUser, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: HandleUser[] = [
    { id: 1, name: "Item1", value: 54, active: true },
    { id: 2, name: "Item2", value: 29, active: false }
];

const result = get_result(testData);
console.log('Processed items:', result);

export { get_result, HandleUser };
