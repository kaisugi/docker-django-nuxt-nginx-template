<template>
  <div>
    <p v-if="$fetchState.pending" class="loading-wrapper">
      <span class="loading"></span>
    </p>
    <p v-else-if="$fetchState.error">Something is wrong.</p>
    <div else>
      <h2>{{ response.message }}</h2>
      <button @click="$fetch">reload</button>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  data() {
    return {
      response: null,
    }
  },
  async fetch() {
    this.response = await this.$axios.$get('/hello/')
  },
})
</script>

<style></style>