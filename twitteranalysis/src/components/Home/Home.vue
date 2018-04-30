<template>
  <!-- <v-container grid-list-md text-md-center fill-height>
    <v-layout row wrap align-content-start>
      <v-flex md4>
        <v-card>
          <v-layout wrap justify-space-around align-center>
          <v-avatar size="250">
            <img src="../../assets/margarita.png" alt="Margarita">
          </v-avatar>
        </v-layout>
        <v-layout row wrap align-center>
          <v-card-text class="px-0">Margarita Zavala</v-card-text>
        </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container> -->

  <!--LOS TRES SEPARADOS  -->
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
        <br>No sabe nada
        <br>Candidata independiente
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
      <v-card-text class="px-0">Ricardo Anaya
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
      <v-card-text>Jaime Rodriguez
        <br>Candidato independiente
        <br>ksmkmka
      </v-card-text>
    </v-layout>
    </v-card>
  </v-flex>
  <!-- candidatos segunda fila -->

</v-layout>
</v-container>
</template>


<style>

.cuadro{
  padding-top: 20px;
  border-radius: 10px 10px 120px 10px;
}
</style>
