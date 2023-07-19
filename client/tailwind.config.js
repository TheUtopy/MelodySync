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
                'wide': 'calc(100vw/5)'
            },
            fontFamily: {
                'sans': ['LeagueGothic-Regular', 'cursive', 'sans-serif'],
                'serif': ['LeagueGothic-Regular', 'cursive', 'sans-serif'],
                'mono': ['LeagueGothic-Regular', 'cursive', 'sans-serif'],
                'display': ['LeagueGothic-Regular', 'cursive', 'sans-serif'],
                'body': ['LeagueGothic-Regular', 'cursive', 'sans-serif'],
                'league-gothic': ['LeagueGothic-Regular', 'sans-serif'],
            },
            variants: {},
            plugins: []
        },
    }
}