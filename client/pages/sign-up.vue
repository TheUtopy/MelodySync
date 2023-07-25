<template>
  <main>
    <Header />
    <section class="bg-pinky-900 h-min py-20 text-pinky-50">
      <article class=" flex flex-col md:flex-row justify-evenly">
        <div class="mx-auto">
          <h2 class="pb-8">Sign Up</h2>
          <form @submit="submitForm" class="text-pinky-1000 font-serif pb-6">
            <FieldInForm label="Username" inputId="username" inputType="text" :input-value="username"
              @update:input-value="username = $event" />
            <FieldInForm label="Email" inputId="email" inputType="email" :input-value="email"
              @update:input-value="email = $event" />
            <FieldInForm label="Password" inputId="password" inputType="password" :input-value="password"
              @update:input-value="password = $event" />
            <FieldInForm label="Confirm Password" inputId="confirmPassword" inputType="password"
              :input-value="confirmPassword" @update:input-value="confirmPassword = $event" />
            <p class="text-pinky-100 mt-[-1.5rem] mb-[2rem]" v-if="showNotMatchingPassword">* Passwords do not match</p>
            <Button color="red" is-submit-button @submit-form="submitForm">Submit</Button>
          </form>
          <h3>Already have an account? <NuxtLink to="/login"
              class="underline hover:no-underline hover:text-pink-700 visited:text-pink-800">Login</NuxtLink>
          </h3>
        </div>
        <div class="pt-[4.4rem] mx-auto flex flex-col items-center">
          <Image source="../static/images/Violin.png" alt="violin" class="max-w-sm lg:max-w-lg" />
          <p class="max-w-sm lg:max-w-lg text-sans text-3xl text-pink-100 text-center pt-8">Don't miss a beat! Sign in now
            and start amplifying your musical journey.</p>
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
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
    };
  },
  computed: {
    showNotMatchingPassword() {
      return this.password !== this.confirmPassword;
    },
  },
  methods: {
    async submitForm(e) {
      e.preventDefault();
      // Vérification des champs requis
      try {
        if (this.username === '') {
          throw new Error('Username is required');
        };
        if (this.email === '') {
          throw new Error('Email is required');
        };
        if (this.password === '') {
          throw new Error('Password is required');
        };
        const regex = /^(?=.*[a-zA-Z])(?=.*\d).{8,}/;
        if (!regex.test(this.password)) {
          throw new Error('Password must at least be 8 characters long and have one digit and one letter');
        };
        if (this.password.length > 24) {
          throw new Error('You password shouldn\'t exceed 24 characters')
        }
        if (this.password !== this.confirmPassword) {
          throw new Error('Passwords don\'t match');
        };
      } catch (error) {
        alert(error);
      }

      // Logique de soumission du formulaire
      if (this.username !== '' && this.email !== '' && this.password !== '' && this.confirmPassword !== '') {
        // Soumettre le formulaire
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password,
        };

        try {
          const response = await fetch('http://localhost:8000/api/user/', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
          });

          const data = await response.json();

          if (response.ok) {
            console.log('Successful inscription');
            this.$router.push('/login');
          } else {
            for (let key in data) {
              alert(data[key]);
            };
          }
        } catch (error) {
          console.log('Error: ', error.response);
        }
      }
    },
  },
};
</script>
