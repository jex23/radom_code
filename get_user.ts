// Random TypeScript interface generated on 2025-10-09

interface CheckConfig {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type CheckConfigResponse = {
    success: boolean;
    data?: CheckConfig;
    error?: string;
};

export { CheckConfig, CheckConfigResponse };
