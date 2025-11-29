// Random TypeScript class generated on 2025-11-29

class GetValue {
    private value: number;
    private readonly createdAt: Date;

    constructor(initialValue: number = 60) {
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

export { GetValue };
