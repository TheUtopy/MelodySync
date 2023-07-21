<template>
  <main>
    <Header />
    <section class="bg-pinky-900 h-min py-20 text-pinky-50">
      <article class=" flex flex-col md:flex-row justify-evenly">
        <div class="mx-auto">
          <h2 class="pb-8">Sign Up</h2>
          <form @submit="submitForm" class="text-pinky-1000 font-serif pb-6">
            <FieldInForm label="Username" inputId="username" inputType="text" :input-value="username" @update:input-value="username = $event"/>
            <FieldInForm label="Email" inputId="email" inputType="email" :input-value="email" @update:input-value="email = $event"/>
            <FieldInForm label="Password" inputId="password" inputType="password" :input-value="password" @update:input-value="password = $event"/>
            <FieldInForm label="Confirm Password" inputId="confirmPassword" inputType="password" :input-value="confirmPassword" @update:input-value="confirmPassword = $event"/>
            <Button color="red" is-submit-button @submit-form="submitForm">Submit</Button>
          </form>
          <h3>Already have an account? <NuxtLink to="/login" class="underline hover:no-underline hover:text-pink-700 visited:text-pink-800">Login</NuxtLink></h3>
        </div>
        <div class="pt-[4.4rem] mx-auto flex flex-col items-center">
          <Image source="../static/images/Violin.png" alt="violin" class="max-w-sm lg:max-w-lg" />
          <p class="max-w-sm lg:max-w-lg text-sans text-3xl text-pink-100 text-center pt-8">Don't miss a beat! Sign in now and start amplifying your musical journey.</p>
        </div>
      </article>
      <Footer class="text-center py-10" />
    </section>
  </main>
</template>

<script>
export default {
  data() {
    return {
      labelActive: false,
      errorMessage: {},
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
      submitForm(e) {
          e.preventDefault();
          // Vérification des champs requis
          if (this.username === '') {
          this.errorMessage['username'] = 'Username is required';
          };
          if (this.email === '') {
          this.errorMessage['email'] = 'Email is required';
          };
          if (this.password === '') {
          this.errorMessage['password'] = 'Password is required';
          };

          // Logique de soumission du formulaire
          if (this.username !== '' && this.email !== '' && this.password !== '' && this.confirmPassword !== '') {
          console.log(this.username, this.email, this.password, this.confirmPassword);
          // Soumettre le formulaire
          }
      },
  },
};
</script>
