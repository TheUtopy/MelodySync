import defaultTheme from 'tailwindcss/defaultTheme'

export default {
    theme: {
        extend: {
            colors: {
                'pinky': {
                    50: '#ffffff',
                    100: '#fff0f3',
                    300: '#ffb3c1',
                    500: '#bf5976',
                    700: '#a4133c',
                    800: '#800F2F',
                    900: '#590d22',
                    1000: '#000000',
                },
            },
            fontSize: {
                'wide': 'calc(100vw/5)',
                'xxl': '250px',
            },
            fontFamily: {
                'sans': ['LeagueGothic-Regular', 'sans-serif'],
                'serif': ['GolosText-Regular', 'sans-serif'],
                'mono': ['GolosText-Regular', 'sans-serif'],
                'display': ['LeagueGothic-Regular', 'sans-serif'],
                'body': ['GolosText-Regular', 'sans-serif'],
                'league-gothic': ['LeagueGothic-Regular', 'sans-serif'],
                'golos-text': ['GolosText-Regular', 'cursive', 'sans-serif'],
            },
            variants: {},
            plugins: []
        },
    }
}