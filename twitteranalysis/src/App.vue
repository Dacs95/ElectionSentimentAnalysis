<template>
  <!-- <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div> -->

  <v-app>
    <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons' rel="stylesheet">
  <!-- <v-navigation-drawer app></v-navigation-drawer> -->
  <v-toolbar>
      <v-toolbar-title>Twitter Analysis</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat href="#/">Home</v-btn>
      </v-toolbar-items>
    </v-toolbar>
  <v-content>
    <v-container fluid>
      <router-view></router-view>
    </v-container>
  </v-content>
  <!-- FOOTER -->
        <v-footer app height="auto" class="grey darken-3" widht="auto">
          <v-layout row wrap justify-center>
            <v-btn
              color="white"
              flat
              v-for="link in links"
              :key="link">
              {{ link }}
            </v-btn>
            <v-flex md12 py-3 text-md-center white--text>
              &copy;2018 — <strong>Vuetify</strong>
            </v-flex>
          </v-layout>
        </v-footer>
</v-app>
</template>

<script>
export default {
  //name: 'App'
   data: () => ({
     links: ['Home', 'About Us', 'Team', 'Services', 'Blog', 'Contact Us']
   })
}


</script>



<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;

}
</style>
