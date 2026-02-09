// Random TypeScript function generated on 2026-02-09

interface DeleteUser {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function create_config(count_rjb: DeleteUser[]): DeleteUser[] {
    const multiplier: number = 5;
    
    return count_rjb
        .filter((item: DeleteUser) => item.active)
        .map((item: DeleteUser, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: DeleteUser[] = [
    { id: 1, name: "Item1", value: 37, active: true },
    { id: 2, name: "Item2", value: 59, active: false }
];

const result = create_config(testData);
console.log('Processed items:', result);

export { create_config, DeleteUser };
