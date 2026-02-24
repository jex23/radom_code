// Random TypeScript function generated on 2026-02-24

interface SetConfig {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function set_value(result_qaa: SetConfig[]): SetConfig[] {
    const multiplier: number = 2;
    
    return result_qaa
        .filter((item: SetConfig) => item.active)
        .map((item: SetConfig, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: SetConfig[] = [
    { id: 1, name: "Item1", value: 78, active: true },
    { id: 2, name: "Item2", value: 29, active: false }
];

const result = set_value(testData);
console.log('Processed items:', result);

export { set_value, SetConfig };
