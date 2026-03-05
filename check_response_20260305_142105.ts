// Random TypeScript class generated on 2026-03-05

class HandleData {
    private value: number;
    private readonly createdAt: Date;

    constructor(initialValue: number = 7) {
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

export { HandleData };
