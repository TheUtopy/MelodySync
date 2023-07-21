<template>
    <nuxt-link
    v-if="!isSubmitButton"
    :to="destination"
    :class="{
        'bg-pinky-800 hover:bg-pinky-500': color === 'burgundy',
        'bg-pinky-1000 hover:bg-pinky-900': color === 'black',
        'bg-pinky-700 hover:bg-pinky-800': color === 'red',
    }"
    class="text-white font-serif text-lg px-4 py-3 rounded-lg transition-colors duration-500"
    >
        <slot></slot>
    </nuxt-link>
    <button
        v-else 
        type="submit"
        :class="{
            'bg-pinky-800 hover:bg-pinky-500': color === 'burgundy',
            'bg-pinky-1000 hover:bg-pinky-900': color === 'black',
            'bg-pinky-700 hover:bg-pinky-800': color === 'red',
        }"
        class="text-white font-serif text-lg px-4 py-3 rounded-lg transition-colors duration-500"
        @click="submitForm"
    >
        <slot></slot>
    </button>
</template>

<script>
export default {
    props: {
        color: {
            type: String,
            default: 'burgundy',
        },
        destination: {
            type: String,
            default: '/',
        },
        isSubmitButton: {
            type: Boolean,
            default: false,
        }
    },
    methods: {
        submitForm(e) {
            this.$emit('submitForm', e)
        }
    }
};
</script>