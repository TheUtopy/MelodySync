<template>
    <main>
        <Header />

        <section class="bg-pinky-900 h-min py-20 text-pinky-50">
            <article class="flex flex-col md:flex-row justify-evenly">
                <div>
                    <h2 class="pb-8">Contact</h2>
                    <form @submit.prevent="submitForm" class="text-pinky-1000 font-serif">
                        <FieldInForm label="Email" inputId="email" inputType="text" :input-value="email" @update:input-value="email = $event" />
                        
                        <div>
                            <label for="message" class="sr-only">Message</label>
                            <textarea id="message" v-model="message" @input="handleMessageInput"  @click="handleFirstClick" required class="p-5 mb-4 rounded-md h-[18rem] w-[30rem]"></textarea>
                        </div>
                        <div ref="messageCount" class="text-sm text-gray-400 hidden">{{ charCount }}/500 characters remaining</div>
                        <br/>
                        <Button color="red" is-submit-button >
                            Submit
                        </Button>
                    </form>
                </div>
                <div class="flex flex-col items-center">
                    <p class="max-w-sm lg:max-w-lg text-sans text-3xl text-pink-100 text-center pb-8">
                        Got a question, concern<br/> or something to report?<br/>We're here to help!
                    </p>
                    <Image source="/static/images/Piano.jpg" alt="piano" class="max-w-sm lg:max-w-sm" />
                </div>
            </article>
        </section>
    </main>
</template>


<script>
export default {
    data() {
        return {
            firstClick: false,
            labelActive: false,
            email: '',
            message: 'Your message goes here.',
        };
    },

    computed: {
        charCount() {
            return 500 - this.message.length;
        }
    },

    methods: {
        async submitForm(e) {
            try {
                this.isFormValid();

                let formData = {
                    email: this.email,
                    message: this.message,
                }

                await this.submitFormData(formData);
            } catch (error) {
                alert(error.message);
            }
        },

        isFormValid() {
            if (!this.email || !this.message.trim() || this.message === 'Your message goes here.') {
                throw new Error('Email and/or message fields are empty.');
            }
        },

        async submitFormData(formData) {
            try {
                const response = await fetch('http://localhost:8000/api/contact/', {
                    method: 'POST',
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(formData),
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data['error']);
                } else {
                    console.log(data)
                    this.$router.push('/contact-sent');
                }
            } catch (error) {
                alert(error.message);
            }
        },

        handleFirstClick() {
            if (!this.firstClick) {
                this.message = '';
                this.firstClick = true;
                this.$refs.messageCount.classList.remove('hidden');
            }
            
        },

        handleMessageInput() {
            if (this.message.length > 500) {
                this.message = this.message.slice(0, 500);
            }
        },
    },
};
</script>