<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark" 
  style="height: 75px;">
    <a class="navbar-brand" href="#">Tweets Visualisation</a>
    <button class="navbar-toggler" type="button">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarItems" >
      <div class="navbar-nav">
        <template v-if="activeNavIndex === 1">
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto" style="color: #ffd04b">Home</a>
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto2">Map</a>
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto3">Analysis</a>
        </template>
        <template v-else-if="activeNavIndex === 2">
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto">Home</a>
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto2" style="color: #ffd04b">Map</a>
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto3">Analysis</a>
        </template>
        <template v-else-if="activeNavIndex === 3">
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto">Home</a>
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto2">Map</a>
          <a class="nav-item nav-link active" href="javascript:void(0)" @click="goto3" style="color: #ffd04b">Analysis</a>
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name:"Navitem",

    data(){
      return {
        activeNavIndex: 1,
      }
    },

    mounted(){
      this.$root.$refs.Navitem = this;
    },

    methods: {
      goto(){
        this.$router.push({
          name:"HomeComponent"   
        })
      },
      goto2(){
        this.$router.push({
          name:"MapComponent"
        })
      },
      goto3(){
        this.$router.push({
          name:"AnalysisComponent"
        })
      },
      changeNavIndex(page) {
        if (page === 'home') {
          this.activeNavIndex = 1;
        } else if (page === 'map') {
          this.activeNavIndex = 2;
        } else {
          this.activeNavIndex = 3;
        }
      }
    }
  }
</script>

