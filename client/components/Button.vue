<template>
    <nuxt-link
    :to="destination"
    :class="{
        'bg-pinky-800 hover:bg-pinky-500': color === 'burgundy',
        'bg-pinky-1000 hover:bg-pinky-900': color === 'black',
    }"
    class="text-white font-serif text-lg px-4 py-3 rounded-lg transition-colors duration-500"
    >
        <slot></slot>
    </nuxt-link>
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
    },
};
</script>