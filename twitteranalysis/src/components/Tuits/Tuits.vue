<template>
  <v-container>
    <v-layout row wrap>
      <v-flex md6 order-lg1>
        <v-layout row>
  <v-flex xs12 sm6 offset-sm3>
    <v-card>
      <v-card-media height="200px">
      <img src="../../assets/margarita.png">
      </v-card-media>
      <v-card-title primary-title>
        <div>
          <div class="headline">Margarita Zavala Gómez</div>
          <span class="texto">Candidata independiente</span>
        </div>
      </v-card-title>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn icon @click.native="show = !show">
          <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-slide-y-transition>
        <v-card-text v-show="show">
          Margarita cuenta actualmente con 1.4 millones de seguidores en Twitter.
        </v-card-text>
      </v-slide-y-transition>
    </v-card>
  </v-flex>
</v-layout>
        <!-- <v-card dark tile flat class="cuadroInfo">
          <v-list-tile>
            <v-list-tile-avatar size="100">
              <img src="../../assets/margarita.png">
            </v-list-tile-avatar>
            <v-list-tile-content class="texto">
              Margarita Zavala Gómez
              <br>1.4 Millones de seguidores
              <br>Candidata independiente
            </v-list-tile-content>
          </v-list-tile>
          </v-card> -->
      </v-flex>

      <v-flex md6 order-lg2>
        <v-list two-line>
          <template v-for="(tuit, index) in tuits">
          <v-card dark tile flat class="cuadroTuit">
            <v-list-tile-content>
                <v-list-tile-title v-html = "tuit.user" class="textoDos"><strong></strong></v-list-tile-title>
                <v-card-text v-html = "tuit.text" class="textoDos"></v-card-text>
            </v-list-tile-content>
          </v-card>
      </template>
    </v-list>
        </v-flex>
    </v-layout>

    <v-layout row class="cuadroDos" justify-center="true">
      <v-flex md6 order-md1>
        <v-card dark tile flat color="grey darken-1" class="cuadroAbajoIzq">
          <template>
            <div id="app">
              <div class="container">
                <div class="Chart__list">
                  <div class="Chart">
                    <h2>Linechart</h2>
                    <line-example></line-example>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import LineExample from '../Charts.js'
export default {
  //name: 'App'
  components: {
  LineExample
  },
   data: () => ({
     tuit: {
       _Id: '',
       name: '',
       text: ''
     },
     tuits: [{
     }],
     show: false,

  }),
  beforeMount(){
  //this.items = //get items from api
  let tuitId = this.tuit.id
  console.log(tuitId)
  this.$store.dispatch('getAllTuits', tuitId).then(tuits => this.tuits = tuits)
}
}
</script>

<style>
.cuadroInfo{
  padding-top: 50px;
  padding-bottom: 50px;
  border-radius: 10px 10px 10px 10px;
  width: 380px;
  background: none !important;
  border-style: solid;
  border-color: #BDBDBD;
}
.texto{
  padding-left: 20px;
  height: 90px;
  color: #D84315;
}
.cuadroTuit{
  padding-top: 50px;
  padding-bottom: 10px;
  padding-left: 20px;
  border-radius: 5px 5px 5px 5px;
  width: 500px;
  left: 130px;
  background: none !important;
  border-bottom: 2px solid;
  border-color: #BDBDBD;
  left: 30px;
}
.textoDos{
  color: #0097A7;
}

.cuadroDos{
  padding-top: 50px;
}

.cuadroAbajoIzq{
  left: 1px;
}

</style>
