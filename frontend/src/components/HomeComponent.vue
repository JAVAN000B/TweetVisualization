<template>
  <div>
    <Navitem class="bar"/>
    <div class="background">
      <el-carousel 
      height="800px" 
      style="position: relative;"
      indicator-position="none">
        <el-carousel-item 
        v-for="item in sentences" 
        :key="item">
          <h3 class="text">{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>
      <el-row>
        <el-col :span="4">
          <div class="grid-content bg-white"></div>
        </el-col>
        <el-col :span="16">
          <div class="grid-content bg-white">
            <h1 style="text-align: center; padding-top: 30px; padding-bottom: 10px; font-weight: lighter">Tweets Visualisation Helps you</h1>
            <h1 style="text-align: center; padding: 10px; font-weight: Normal">Explore the interesting side behind Australians' lives</h1>
            <h4 style="text-align: center; padding: 5px; font-weight: Normal; color: grey">COMP90024 Project Team 29 Presents</h4>
            <el-row style="padding: 14px;" >
              <el-col :span="12" style="padding-left: 5%; padding-right: 5%">
                <el-card :body-style="{ padding: '0px' }" class="box-card">
                  <img src="../assets/world.jpg" class="image">
                  <div style="padding-left: 30%; padding-right: 30%; padding-top: 14px; padding-bottom: 14px">
                    <div class="bottom clearfix">
                      <el-button type="text" class="button"><a href="javascript:void(0)" @click="goto2">Try with Interactive Map</a></el-button>
                    </div>
                  </div>
                </el-card>
              </el-col>
              <el-col :span="12" style="padding-left: 5%; padding-right: 5%">
                <el-card :body-style="{ padding: '0px' }" class="box-card">
                  <img src="../assets/analysis.jpg" class="image">
                  <div style="padding-left: 30%; padding-right: 30%; padding-top: 14px; padding-bottom: 14px">
                    <div class="bottom clearfix">
                      <el-button type="text" class="button"><a href="javascript:void(0)" @click="goto3">Try with Data Analysis Tools</a></el-button>
                    </div>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <h1 style="text-align: center; padding: 20px; font-weight: Normal">Who are we?</h1>
            <el-row>
              <el-col :span="8">
                <div style="margin-left: 35%;">
                  <el-avatar src="https://robohash.org/4a48c4856e635cc9f46ccd6b40cbc303?set=set4&bgset=&size=400x400" :size="100"></el-avatar>
                </div>
                <h4 style="text-align: center">Man Xu</h4>
              </el-col>
              <el-col :span="8">
                <div style="margin-left: 32%;">
                  <el-avatar src="https://robohash.org/7eb3b7cfe093e699093dc77ebdc2450c?set=set4&bgset=&size=400x400" :size="100"></el-avatar>
                </div>
                <h4 style="text-align: center">Xuanyu Chen</h4>
              </el-col>
              <el-col :span="8">
                <div style="margin-left: 32%;">
                  <el-avatar src="https://robohash.org/ebd9bee59cb2e199586042ca9527a31c?set=set4&bgset=&size=400x400" :size="100"></el-avatar>
                </div>
                <h4 style="text-align: center">Minghui Sun</h4>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="12">
                <div style="margin-left: 40%;">
                  <el-avatar src="https://robohash.org/61aa5a0011e2e5f9420f752afebae4aa?set=set4&bgset=&size=400x400" :size="100"></el-avatar>
                </div>
                <h4 style="text-align: center">Da Xu</h4>
              </el-col>
              <el-col :span="12">
                <div style="margin-left: 40%;">
                  <el-avatar src="https://robohash.org/f1a13f48db0daf795f827045c635f13a?set=set4&bgset=&size=400x400" :size="100"></el-avatar>
                </div>
                <h4 style="text-align: center">Shanshan Zhang</h4>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-white"></div>
        </el-col>
      </el-row>
      <el-footer><p>&copy; University of Melbourne, 2021</p></el-footer>
    </div>
    
  </div>

</template>

<script>
  import Navitem from './Navitem'

  export default {
    name: 'AnalysisComponent',
    components: {Navitem},
    data(){
      return {
          sentences: ['Explore the world', 'Feel the beauty of big data', 'Check the tweets around you', 'Your story starts from here'],
          currentDate: new Date(),
      }
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
      }
    }
  }

</script>


<style>
  .background{
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    margin-top: 75px;
  }


  .el-carousel__item h3 {
    font-size: 50px;
    opacity: 0.9;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(4n) {
    background-image: url(../assets/data.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    color: white;
  }
  
  .el-carousel__item:nth-child(4n+1) {
    background-image: url(../assets/melbourne.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    color: white;
  }

  .el-carousel__item:nth-child(4n+2) {
    background-image: url(../assets/sydney.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    color: white;
  }

  .el-carousel__item:nth-child(4n+3) {
    background-image: url(../assets/map.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    color: white;
  }

  .text {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .grid-content {
    border-radius: 4px;
    min-height: 35px;
  }

  .bg-white {
    background: white;
  }
  .bg-purple {
    background: #d3dce6;
  }

  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    line-height: 12px;
  }

  .button {
    padding: 0;
  }

  .image {
    width: 100%;
    height: 250px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .box-card {
    width: 400px;
  }

  .el-footer {
    background-color: #1f2225;
    color: white;
    text-align: center;
    line-height: 60px;
    margin-top: 10px;
  }



</style>
