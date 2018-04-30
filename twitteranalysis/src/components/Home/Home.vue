<template>
  <!--Los tres candidatos de arriba -->
  <v-container grid-list-md text-md-center>
  <v-layout row wrap align-content-start>
  <v-flex md4 order-md1 order-md1>
    <v-card dark tile flat color="grey darken-1" class="cuadro">
      <v-layout wrap justify-space-around align-center>
      <v-avatar size="250">
        <img src="../../assets/margarita.png" alt="Margarita">
      </v-avatar>
    </v-layout>
    <v-layout row wrap align-center>
      <v-card-text class="px-0">Margarita Zavala Gómez
        <br>Candidata independiente
        <br>Esposa de Calderón
    </v-card-text>
    </v-layout>
    </v-card>
  </v-flex>
  <v-flex md4 order-md2 order-md2>
    <v-card dark tile flat color="grey darken-1" class="cuadro">
      <v-layout wrap justify-space-around align-center>
      <v-avatar size="250">
        <img src="../../assets/anaya.png" alt="Anaya">
      </v-avatar>
    </v-layout>
    <v-layout row wrap align-center>
      <v-card-text class="px-0">Ricardo Anaya Cortés
        <br>Candidato del PAN
        <br>El mejor de todos
      </v-card-text>
    </v-layout>
    </v-card>
  </v-flex>
  <v-flex md4 order-md3 order-md3>
    <v-card dark tile flat color="grey darken-1" class="cuadro">
      <v-layout wrap justify-space-around align-center>
      <v-avatar size="250">
        <img src="../../assets/bronco.png" alt="Bronco">
      </v-avatar>
    </v-layout>
    <v-layout row wrap align-center>
      <v-card-text>Jaime Rodriguez Calderón
        <br>Candidato independiente
        <br>ksmkmka
      </v-card-text>
    </v-layout>
    </v-card>
  </v-flex>
</v-layout>

<!-- Dos candidatos segunda fila -->
<v-layout row class="cuadroDos" justify-center="true">
    <v-flex md6 order-md1>
      <v-card dark tile flat color="grey darken-1" class="cuadroAbajoIzq">
        <v-layout wrap justify-space-around align-center>
        <v-avatar size="250">
          <img src="../../assets/amlo.png" alt="AMLO">
        </v-avatar>
      </v-layout>
      <v-layout row wrap align-center>
        <v-card-text>Manuel Lopez Obrador
          <br>Candidato de Morena
          <br>COMUNISTA
        </v-card-text>
      </v-layout>
      </v-card>
    </v-flex>
    <v-flex md6 order-md2>
      <v-card dark tile flat color="grey darken-1" class="cuadroAbajoDer">
        <v-layout wrap justify-space-around align-center>
        <v-avatar size="250">
          <img src="../../assets/meade.png" alt="Meade">
        </v-avatar>
      </v-layout>
      <v-layout row wrap align-center>
        <v-card-text>Antonio Meade Kuribreña
          <br>Candidato del PRI
          <br><strong>The worst of them all</strong>
        </v-card-text>
      </v-layout>
      </v-card>
    </v-flex>
  </v-layout>
</v-container>
</template>


<style>

.cuadro{
  padding-top: 20px;
  border-radius: 10px 10px 120px 10px;
}

.cuadroAbajoIzq{
  width: 380px;
  border-radius: 10px 10px 120px 10px;
  left: 190px;
}

.cuadroAbajoDer{
  width: 380px;
  border-radius: 10px 10px 120px 10px;
}

.cuadroDos{
  padding-top: 50px;
}
</style>
