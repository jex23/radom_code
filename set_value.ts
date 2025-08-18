// Random TypeScript function generated on 2025-08-18

interface ProcessRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function check_config(config_omd: ProcessRequest[]): ProcessRequest[] {
    const multiplier: number = 2;
    
    return config_omd
        .filter((item: ProcessRequest) => item.active)
        .map((item: ProcessRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ProcessRequest[] = [
    { id: 1, name: "Item1", value: 100, active: true },
    { id: 2, name: "Item2", value: 47, active: false }
];

const result = check_config(testData);
console.log('Processed items:', result);

export { check_config, ProcessRequest };
