export default function ({ app, redirect }) {
    const sessionId = app.$cookies.get('sessionid');
    if (sessionId) {
        redirect('/empty');
    }
}
