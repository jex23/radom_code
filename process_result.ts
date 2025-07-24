// Random TypeScript function generated on 2025-07-24

interface CreateUser {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function handle_user(result_nvc: CreateUser[]): CreateUser[] {
    const multiplier: number = 10;
    
    return result_nvc
        .filter((item: CreateUser) => item.active)
        .map((item: CreateUser, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: CreateUser[] = [
    { id: 1, name: "Item1", value: 38, active: true },
    { id: 2, name: "Item2", value: 64, active: false }
];

const result = handle_user(testData);
console.log('Processed items:', result);

export { handle_user, CreateUser };
