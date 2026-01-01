// Random TypeScript function generated on 2026-01-01

interface SetResult {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function get_user(value_xpn: SetResult[]): SetResult[] {
    const multiplier: number = 4;
    
    return value_xpn
        .filter((item: SetResult) => item.active)
        .map((item: SetResult, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: SetResult[] = [
    { id: 1, name: "Item1", value: 49, active: true },
    { id: 2, name: "Item2", value: 21, active: false }
];

const result = get_user(testData);
console.log('Processed items:', result);

export { get_user, SetResult };
