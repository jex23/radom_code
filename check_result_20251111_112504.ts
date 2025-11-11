// Random TypeScript interface generated on 2025-11-11

interface HandleUser {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type HandleUserResponse = {
    success: boolean;
    data?: HandleUser;
    error?: string;
};

export { HandleUser, HandleUserResponse };
