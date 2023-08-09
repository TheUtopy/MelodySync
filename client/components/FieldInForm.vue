<template>
  <div class="relative pb-8">

    <label :for="inputId"
      :class="{ 'top-[-20px] left-0 bg-pinky-700 px-2 text-pinky-100 rounded-lg border-4 border-pinky-1000 text-[0.8rem]': inputValue !== '' || labelActive }"
      class="absolute top-4 left-5 transition-all pointer-events-none text-xl">
      {{ label }}
    </label>

    <input :type="inputType" :id="inputId" :value="inputValue" @input="$emit('update:inputValue', $event.target.value)"
      required @focus="labelActive = true" @blur="labelActive = false" class="p-5 rounded-md">

    <p class="text-pinky-100 mt-2" v-if="showRequiredMessage">* {{ label }} is required</p>
    <p class="text-pinky-100 mt-2 text-xs" v-if="showPasswordRequirements">* {{ label }} should have at least one
      letter<br>and
      one
      digit and be at least 8 characters long</p>
  </div>
</template>
  
<script>
export default {
  props: {
    label: {
      type: String,
      required: true,
    },
    inputId: {
      type: String,
      required: true,
    },
    inputType: {
      type: String,
      required: true,
    },
    inputValue: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      labelActive: false,
    };
  },
  computed: {
    showRequiredMessage() {
      return this.inputValue === '' && this.$route.path === '/sign-up' && this.inputId !== "confirmPassword";
    },
    showPasswordRequirements() {
      const regex = /^(?=.*[a-zA-Z])(?=.*\d).{8,}/;
      return this.inputId === "password" && !regex.test(this.inputValue) && this.$route.path === '/sign-up' && this.inputValue !== "";
    }
  }
};
</script>