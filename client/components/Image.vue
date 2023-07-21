<template>
    <img :src="source" class="rounded-3xl mix-blend-luminosity" :alt="alt">
</template>

<script>
export default {
    props: {
        source: {
            type: String,
            required: true,
        },
        alt: {
            type: String,
            required: true,
        },
    },
};
</script>