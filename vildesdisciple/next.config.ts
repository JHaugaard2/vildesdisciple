import { NextConfig } from 'next';

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/camera/stream',
        destination: 'http://192.168.1.63:8000/stream', // your Pi camera stream
      },
    ];
  },
};

export default nextConfig;
