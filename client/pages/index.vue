<template>
  <main>
  <section class="max-w-5xl h-min mx-auto flex flex-col">
    <Header />

    <p class="text-xl mx-10 max-w-3xl">
        Welcome to Melody Sync, the ultimate community for music learners. Exchange tips, showcase accomplishments,
        and
        celebrate the joys of mastering musical instruments. Dive in and join the melody!
    </p>

    <div class="ml-10 my-20">
      <Button color="burgundy" destination="/sign-up">Sign Up</Button>
      <Button color="black" destination="/login" class="ml-8">Login</Button>
    </div>
  </section>


  <section class="bg-pinky-900 h-min text-pinky-50 text-lg py-24">
    <div class="grid grid-cols-2 grid-rows-2 w-4/5 mx-auto gap-16">
      <Image source="../static/images/Orchestra.png" alt="orchestra" />

      <article class="flex flex-col justify-center">
        <h2>Share Advice, Learn Faster, and Make Friends</h2>
        <p class="mt-6">Melody Sync brings together ambitious learners to motivate, inspire, and support each
          other on their musical journeys. Why learn alone when you can grow together?</p>
      </article>

      <div class="flex flex-col justify-center text-right">
        <h2>Create Profiles to Display Your Instrument Mastery</h2>
        <p class="mt-6">Show off your favorite instrument and the skills you're acquiring. Be proud of your
          progress and encourage others to reach new heights!</p>
      </div>
      
      <Image source="../static/images/Guitar.png" alt="guitar" />
    </div>
  </section>


  <section class="bg-pinky-300 h-min py-24">
    <div class="max-w-5xl mx-auto">
      <h2 class="text-5xl">Ready to join the tune? Sync up with Melody now!</h2>

      <div class="mb-28 mt-10">
        <Button color="red" destination="/sign-up">Sign Up</Button>
        <Button color="black" destination="/login" class="ml-8">Login</Button>
      </div>

      <h2 class="text-5xl pb-16">Questions? We got answers!</h2>

      <article class="grid grid-cols-2 grid-rows-2 gap-20">
        <div class="max-w-md">
          <h3>Is Melody Sync free to join?</h3>
          <p class="text-pinky-1000">Yes, creating an account and participating is absolutely free!</p>
        </div>

        <div class="max-w-md">
          <h3>Can I share my performances?</h3>
          <p class="text-pinky-1000">Of course! The platform encourages users to share their progress and performances with others.</p>
        </div>

        <div class="max-w-md">
          <h3>Do I need any prior experience?</h3>
          <p class="text-pinky-1000">Not at all! Melody Sync welcomes learners of all levels, from beginners to experienced musicians.</p>
        </div>

        <div class="max-w-md">
          <h3>Can I learn multiple instruments?</h3>
          <p class="text-pinky-1000">Definitely! The community supports learning and sharing tips for various instruments.</p>
        </div>
      </article>

      <Footer />
    </div>
  </section>
  </main>
</template>

<style>
.index-image {
  border-radius: 1.5rem;
  mix-blend-mode: luminosity;
  min-height: auto;
  max-width: 28rem;
}
</style>
  