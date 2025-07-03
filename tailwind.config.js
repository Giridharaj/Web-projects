/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        quantum: {
          blue: '#00D4FF',
          purple: '#8B5CF6',
          pink: '#EC4899',
          dark: '#0F0F23',
          darker: '#0A0A1B',
        }
      },
      animation: {
        'particle-float': 'particle-float 20s infinite linear',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite alternate',
        'circuit-flow': 'circuit-flow 3s ease-in-out infinite',
      },
      keyframes: {
        'particle-float': {
          '0%': { transform: 'translateY(100vh) translateX(-10px)' },
          '100%': { transform: 'translateY(-100px) translateX(10px)' },
        },
        'pulse-glow': {
          '0%': { boxShadow: '0 0 20px rgba(0, 212, 255, 0.3)' },
          '100%': { boxShadow: '0 0 40px rgba(0, 212, 255, 0.6)' },
        },
        'circuit-flow': {
          '0%, 100%': { opacity: 0.3 },
          '50%': { opacity: 1 },
        },
      },
      backdropBlur: {
        xs: '2px',
      }
    },
  },
  plugins: [],
};