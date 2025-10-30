// Random TypeScript function generated on 2025-10-30

interface ProcessUser {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function create_config(node_vpv: ProcessUser[]): ProcessUser[] {
    const multiplier: number = 4;
    
    return node_vpv
        .filter((item: ProcessUser) => item.active)
        .map((item: ProcessUser, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ProcessUser[] = [
    { id: 1, name: "Item1", value: 28, active: true },
    { id: 2, name: "Item2", value: 40, active: false }
];

const result = create_config(testData);
console.log('Processed items:', result);

export { create_config, ProcessUser };
