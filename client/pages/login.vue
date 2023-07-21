<template>
    <main>
        <Header />
        <section class="bg-pinky-900 h-min py-20 text-pinky-50 pl-20">
            <h2 class="pb-8">Login</h2>
            <form @submit="submitForm" class="text-pinky-1000 font-serif">
                <FieldInForm label="Username" inputId="username" inputType="text" :input-value="username" @update:input-value="username = $event"/>
                <FieldInForm label="Password" inputId="password" inputType="password" :input-value="password" @update:input-value="password = $event"/>
            </form>
        </section>
    </main>
</template>

<script>
export default {
    data() {
        return {
            labelActive: false,
            errorMessage: {},
            username: '',
            password: '',
        };
    },
    methods: {
        submitForm(e) {
            e.preventDefault();
        },
    },
};
</script>