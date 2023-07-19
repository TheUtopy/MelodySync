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
                    900: '#590d22',
                    1000: '#000000',
                },
            },
            fontFamily: {
                'sans': ['LeagueGothic-Regular', 'sans-serif'],
                'serif': ['LeagueGothic-Regular', 'sans-serif'],
                'mono': ['LeagueGothic-Regular', 'sans-serif'],
                'display': ['LeagueGothic-Regular', 'sans-serif'],
                'body': ['LeagueGothic-Regular', 'sans-serif'],
                'league-gothic': ['LeagueGothic-Regular', 'sans-serif'],
            },
            backgroundColor: {
                'default': 'red-500',
            }
        }
    }
}