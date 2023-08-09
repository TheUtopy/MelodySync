<template>
    <main class="flex flex-col min-h-screen">
        <Header/>
        <section class="bg-pinky-900 py-20 text-center text-pinky-50 h-min flex-grow flex flex-col justify-center">
            <h2 class="pb-8 text-5xl">Your email has been sent</h2>
            <p class="text-xl pb-6">Thank you for contacting us.</p>

            <nuxt-link to="/" class="text-2xl text-pinky-500 underline hover:no-underline hover:text-pink-300 visited:text-pink-500">
                Go back to the home page.
            </nuxt-link>
        </section>
    </main>
</template>