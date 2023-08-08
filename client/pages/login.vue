<template>
    <main>
        <Header />
        <section class="bg-pinky-900 h-min py-20 text-pinky-50 pl-20">
            <article class="flex flex-col md:flex-row justify-evenly">
                <div>
                    <h2 class="pb-8">Login</h2>
                    <form @submit.prevent="submitForm" class="text-pinky-1000 font-serif">
                        <FieldInForm label="Username" inputId="username" inputType="text" :input-value="username"
                            @update:input-value="username = $event" />
                        <FieldInForm label="Password" inputId="password" inputType="password" :input-value="password"
                            @update:input-value="password = $event" />
                        <div class="pb-6">
                            <input type="checkbox" id="stayConnected" v-model="stayConnected">
                            <label for="stayConnected" class="pl-2 text-pinky-100 text-lg">Stay connected</label>
                        </div>
                        <Button color="red" is-submit-button @submit-form="submitForm">
                            Submit
                        </Button>
                    </form>
                    <h3 class="mt-6 text-center">You don't have an account yet?
                        <NuxtLink to="/sign-up"
                            class="underline hover:no-underline hover:text-pink-700 visited:text-pink-800">
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
            username: '',
            password: '',
            stayConnected: false,
        };
    },
    methods: {
        async submitForm(e) {
            try {
                this.isFormValid();

                let formData = {
                    username: this.username,
                    password: this.password,
                }

                if (this.stayConnected) {
                    formData.stay_connected = this.stayConnected;
                }

                await this.submitFormData(formData);
            } catch (error) {
                alert(error.message);
            }
        },

        isFormValid() {
            if (this.username === '' || this.password === '') {
                throw new Error('Username and/or password fields are empty.');
            }
        },

        async submitFormData(formData) {
            try {
                const response = await fetch('http://localhost:8000/api/user/login/', {
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(formData),
                    credentials: 'include',
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data['error']);
                } else {
                    console.log('Successful login!');
                    this.$router.push('/empty');
                }
            } catch (error) {
                if (error.message === 'Invalid Credentials') {
                    alert('Username/Password combination doesn\'t match in the database.');
                } else if (error.message === 'Missing Credentials') {
                    alert('Please enter your username and password.');
                }
            }
        },
    },
};
</script>