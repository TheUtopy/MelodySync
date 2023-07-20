<template>
    <section class="max-w-5xl h-min mx-auto flex flex-col">
        <div class="text-center">
            <h1 class="my-auto text-wide whitespace-nowrap lg:text-xxl xl:text-xxl">
                MELODY SYNC
            </h1>
        </div>

        <p class="text-xl font-serif mx-10 max-w-3xl">
            Welcome to Melody Sync, the ultimate community for music learners. Exchange tips, showcase accomplishments,
            and
            celebrate the joys of mastering musical instruments. Dive in and join the melody!
        </p>

        <div class="ml-10 my-20">
          <Button color="burgundy" destination="/sign-up">Sign Up</Button>
          <Button color="black" destination="/login" class="ml-8">Login</Button>
        </div>
      </section>


    <section class="bg-pinky-900 h-min text-pinky-50 text-lg py-24 mx-auto">
      <div class="grid grid-cols-2 grid-rows-2 w-4/5 mx-auto gap-16">
        <img src="../static/images/Orchestra.png" class="index-image justify-self-end" alt="orchestra">

        <article class="flex flex-col justify-center">
          <h2 class="text-4xl">Share Advice, Learn Faster, and Make Friends</h2>
          <p class="font-serif mt-6">Melody Sync brings together ambitious learners to motivate, inspire, and support each
            other on their musical journeys. Why learn alone when you can grow together?</p>
        </article>

        <div class="flex flex-col justify-center text-right">
          <h2 class="text-4xl">Create Profiles to Display Your Instrument Mastery</h2>
          <p class="font-serif mt-6">Show off your favorite instrument and the skills you’re acquiring. Be proud of your
            progress and encourage others to reach new heights!</p>
        </div>
        
        <img src="../static/images/Guitar.png" class="index-image justify-self-start" alt="guitar">
      </div>
    </section>
</template>

<style>
.index-image {
  border-radius: 1.5rem;
  mix-blend-mode: luminosity;
  min-height: auto;
  max-width: 28rem;
}
</style>
  