<template>
  <v-app>
    <v-app-bar app color="primary">
      <router-link to="/" class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
          to="/"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </router-link>

      <v-spacer></v-spacer>

      <UserDialog v-if="isAuthenticated" />
      <LoginButton v-else />
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import UserDialog from "./components/UserDialog";
import LoginButton from "./components/LoginButton";

export default {
  name: "App",

  components: {
    UserDialog,
    LoginButton,
  },

  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
  },

  methods: {
    ...mapActions("auth", ["logout", "getUserProfile"]),
  },

  mounted() {
    if (this.isAuthenticated) {
      this.getUserProfile()
      .catch(err => {
        console.log(err)
      })
    }
  },

  data: () => ({
    //
  }),
};
</script>
