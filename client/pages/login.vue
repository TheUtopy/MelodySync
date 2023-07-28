<template>
    <main>
        <Header />
        <section class="bg-pinky-900 h-min py-20 text-pinky-50 pl-20">
            <article class="flex flex-col md:flex-row justify-evenly">
                <div>
                    <h2 class="pb-8">Login</h2>
                    <form @submit="submitForm" class="text-pinky-1000 font-serif">
                        <FieldInForm 
                            label="Username" 
                            inputId="username" 
                            inputType="text" 
                            :input-value="username" 
                            @update:input-value="username = $event"
                        />
                        <FieldInForm 
                            label="Password" 
                            inputId="password" 
                            inputType="password" 
                            :input-value="password" 
                            @update:input-value="password = $event"
                        />
                        <Button color="red" is-submit-button @submit-form="submitForm">
                            Submit
                        </Button>
                    </form>
                    <h3 class="mt-6 text-center">You don't have an account yet? 
                        <NuxtLink 
                            to="/sign-up" 
                            class="underline hover:no-underline hover:text-pink-700 visited:text-pink-800"
                        >
                            Sign up
                        </NuxtLink>
                    </h3>
                </div>
                <div>
                    <p class="max-w-sm lg:max-w-lg text-sans text-3xl text-pink-100 text-center pb-8">
                        Login, fellow maestro! Unleash your musical journey and share your harmony with the world.
                    </p>
                    <Image source="/static/images/Guitar2.jpg" alt="guitar" class="max-w-sm lg:max-w-lg" />
                </div>
            </article>
            <div class="text-center pt-10">
                <Footer />
            </div>
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