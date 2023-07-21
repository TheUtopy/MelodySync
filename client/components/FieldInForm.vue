<template>
    <div class="relative pb-8">
        <label :for="inputId" :class="{'top-[-20px] left-0 text-md bg-pinky-700 px-2 text-pinky-100 rounded-lg border-4 border-pinky-1000': inputValue !== '' || labelActive}" class="absolute top-4 left-5 transition-all pointer-events-none text-xl">{{ label }}</label>
        <input :type="inputType" :id="inputId" :value="inputValue" @input="$emit('update:inputValue', $event.target.value)" required 
            @focus="labelActive = true" @blur="labelActive = false"
            class="p-5 rounded-md">
        <p class="text-pinky-100 mt-2" v-if="showRequiredMessage">* {{ label }} is required</p>
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
        errorMessage: {},
      };
    },
    computed: {
      showRequiredMessage() {
        return  this.inputValue === '' && this.$route.path === '/sign-up';
      }
    }
  };
  </script>