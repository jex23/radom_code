// Random TypeScript class generated on 2025-12-09

class UpdateData {
    private value: number;
    private readonly createdAt: Date;

    constructor(initialValue: number = 59) {
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

export { UpdateData };
