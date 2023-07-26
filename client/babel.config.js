module.exports = {
    presets: [
        ['@babel/preset-env', { targets: { node: 'current' } }],
        ['@babel/preset-react', { runtime: 'automatic' }],
    ],
    plugins: [
        ['@babel/plugin-syntax-jsx', { runtime: 'automatic' }],
    ]
};