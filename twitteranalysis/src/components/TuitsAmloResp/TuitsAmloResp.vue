<template>
  <v-container>
    <v-layout row wrap>
      <v-flex md6 order-lg1>
        <v-layout row>
  <v-flex xs12 sm6 offset-sm3 class="bloqueCan">
    <v-card>
      <v-card-media height="200px">
      <img src="../../assets/amlo.png">
      </v-card-media>
      <v-card-title primary-title>
        <div>
          <div class="headline">Andres Manuel Lopez Obrador</div>
          <span class="texto">Candidato de Morena</span>
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
          Es un idiota.
        </v-card-text>
      </v-slide-y-transition>
    </v-card>
  </v-flex>
</v-layout>
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

      <!-- Despliegue de tuits -->
      <v-flex md6 order-lg2>
        <v-layout row>
          <v-flex  offset-sm2 xs12 sm12>
        <v-list two-line>
          <template v-for="(tuitResp, index) in tuitsResp">
          <v-card dark tile flat class="cuadroTuit">
            <v-list-tile-content>
                <v-list-tile-title v-html = "tuitResp.user.name" class="textoDos"><strong></strong></v-list-tile-title>
                <v-card-text v-html = "tuitResp.text" class="textoDos"></v-card-text>

                <v-layout row wrap>
                  <v-flex md2 order-md1 class="rtext">
                      <v-card-text v-html = "tuitResp.retweet_count" class="textoTres">
                      </v-card-text>
                  </v-flex>
                  <v-flex md2 order-md2 class="rt">
                      <v-icon color="green">cached</v-icon>
                  </v-flex>
                  <v-flex md2 order-md3 class="ltext">
                    <v-card-text v-html = "tuitResp.favorite_count" class="textoCuatro">
                    </v-card-text>
                  </v-flex>
                  <v-flex md2 order-md4 class="like">
                    <v-icon color="red">favorite_border</v-icon>
                  </v-flex>
                  <v-flex md2 order-md4 class="like">
                    <v-tooltip bottom>
                      <v-btn  flat icon color="orange" slot="activator" href="#/tuitsAmloResp">
                         <v-icon>trending_up</v-icon>
                      </v-btn>
                      <span>Análisis</span>
                    </v-tooltip>
                  </v-flex>
                </v-layout>

            </v-list-tile-content>
          </v-card>
      </template>
    </v-list>
  </v-flex>
  </v-layout>
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
     tuitResp: {
       _Id: '',
       name: '',
       text: ''
     },
     tuitsResp: [{
     }],
     show: false,

  }),
  beforeMount(){
  //this.items = //get items from api
  let candId = 'lopezobrador_'
  console.log(candId)
  this.$store.dispatch('getAllTuitsResp', candId).then(tuitsResp => this.tuitsResp = tuitsResp)
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
  width: 430px;
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
  padding-top: 10px !important;
}

.bloqueCan{
  padding-bottom: 100px;
}

</style>
