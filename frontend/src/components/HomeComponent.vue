<template>
  <div>
    <Navitem class="bar"/>
    <div class="background"></div>
    
  </div>

</template>

<script>
  import Navitem from './Navitem'

  export default {
    components: {Navitem},
  }

</script>


<style>
  .background{
    position:fixed;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    z-index:-10;
    background-image: url(../assets/melbourne.jpg);
    background-size: cover;
    background-position: center;
  }

  .center{
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%,-50%);
  }

</style>
