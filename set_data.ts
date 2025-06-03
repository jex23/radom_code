// Random TypeScript class generated on 2025-06-03

class DeleteData {
    private value: number;
    private readonly createdAt: Date;

    constructor(initialValue: number = 88) {
        this.value = initialValue;
        this.createdAt = new Date();
    }

    public getValue(): number {
        return this.value;
    }

    public updateValue(newValue: number): void {
        this.value = newValue;
    }

    public getInfo(): object {
        return {
            value: this.value,
            createdAt: this.createdAt.toISOString()
        };
    }
}

export { DeleteData };
