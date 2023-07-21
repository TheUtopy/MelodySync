<template>
    <h3 class="text-3xl mt-20" v-if="isIndexVue">Got another question? 
        <nuxt-link to="/contact" class="underline hover:no-underline hover:text-pink-800 visited:text-pink-700">
          You can contact us here.
        </nuxt-link>
    </h3>
    <h3 class="text-3xl mt-20" v-else>Got any question? 
        <nuxt-link to="/contact" class="underline hover:no-underline hover:text-pink-800 visited:text-pink-700">
          You can contact us here.
        </nuxt-link>
    </h3>
</template>

<script>
export default {
    computed: {
        isIndexVue() {
            return this.$route.path === '/';
        }
    }
}
</script>