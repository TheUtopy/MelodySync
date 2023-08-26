<template>
    <main>
        <section class="bg-pinky-900 py-20 text-center text-pinky-50">
            <form @submit.prevent="submitForm" class="text-pinky-1000 font-serif">
                <textarea id="message" v-model="message" required
                    class="p-5 mb-4 rounded-md h-[18rem] w-[30rem]"></textarea>
                <Button color="red" is-submit-button>
                    Submit
                </Button>
            </form>
        </section>
    </main>
</template>

<script>
export default {
    data() {
        return {
            message: '',
        }
    },
    methods: {
        async submitForm(e) {
            try {
                let formData = {
                    message: this.message,
                }

                const response = await fetch('http://localhost:8000/api/post/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData),
                    credentials: 'include',
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data['error']);
                } else {
                    console.log(data);
                }
            } catch (error) {
                alert(error.message);
            }
        },
    }
}
</script>