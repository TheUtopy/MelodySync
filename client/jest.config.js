module.exports = {
    preset: '@nuxt/test-utils',
    moduleFileExtensions: ['js', 'jsx'],
    transform: {
        '^.+\\.jsx?$': 'babel-jest',
    },
    transformIgnorePatterns: ['/node_modules/(?!@nuxt)'],
};