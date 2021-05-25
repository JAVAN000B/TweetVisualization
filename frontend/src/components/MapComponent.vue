<template>
  <div>
    <div id="map"></div>
    <Navitem class="bar"/>
    <div id="clickables">
      <el-radio-group 
      v-model="isCollapse"
      text-color="#fff"
      fill="#545c64"
      style="position: absolute; left: 20px;">
        <el-radio-button :label="false">Expand</el-radio-button>
        <el-radio-button :label="true">Collapse</el-radio-button>
      </el-radio-group>
      <el-menu 
      class="el-menu-vertical-demo" 
      @open="handleOpen" @close="handleClose" 
      :collapse="isCollapse" 
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      style="position: absolute; left: 20px; margin-top: 50px">

        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span slot="title" style="font-size: 17px;">Area</span>
          </template>
          <el-submenu index="1-1">
            <span slot="title" style="font-size: 17px;" >Australia</span>
            <el-menu-item-group>
              <span slot="title" style="font-size: 15px;">
                <i class="el-icon-caret-bottom"></i>
                Pop & Income
              </span>
              <el-menu-item index="1-1-1-1" @click="curLabel='size', switchTo('states')">
                <i class="el-icon-s-data"></i>
                Size
              </el-menu-item>
              <el-menu-item index="1-1-1-2" @click="curLabel='age', switchTo('states')">
                <i class="el-icon-s-data"></i>
                Age
              </el-menu-item>
              <el-menu-item index="1-1-1-3" @click="curLabel='income', switchTo('states')">
                <i class="el-icon-s-data"></i>
                Income
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu >
          <el-submenu  index="1-2">
            <span slot="title" style="font-size: 17px;">Melbourne</span>
            <el-menu-item-group>
              <span slot="title" style="font-size: 15px; text-align: center">
                <i class="el-icon-caret-bottom"></i>
                Pop & Income
              </span>
              <el-menu-item index="1-2-1"  @click="curLabel='size', switchTo('mel')">
                <i class="el-icon-s-data"></i>
                Size
              </el-menu-item>
              <el-menu-item index="1-2-2" @click="curLabel='age', switchTo('mel')">
                <i class="el-icon-s-data"></i>
                Age
              </el-menu-item>
              <el-menu-item index="1-2-3" @click="curLabel='income', switchTo('mel')">
                <i class="el-icon-s-data"></i>
                Income
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span slot="title" style="font-size: 17px;">Content</span>
          </template>
          <el-submenu index="2-1">
            <span slot="title" style="font-size: 17px;" >Twitter</span>
              <el-menu-item index="2-1-1-1" @click="addMarkers1()">
                <i class="el-icon-s-data"></i>
                Total number of tweets
              </el-menu-item>
              <el-menu-item index="2-1-1-2" @click="addMarkers2()">
                <i class="el-icon-s-data"></i>
                Top 5 Emoji 
              </el-menu-item>
              <el-menu-item index="2-1-1-3" @click="addMarkers3()">
                <i class="el-icon-s-data"></i>
                Top 5 Hashtag 
              </el-menu-item>
              <el-menu-item index="2-1-1-4" @click="addMarkers4()">
                <i class="el-icon-s-data"></i>
                Top 5 Vulgar Word 
              </el-menu-item>
          </el-submenu >
        </el-submenu>
      </el-menu>
    </div>


    <div class="modal fade" id="detailInfoModal" tabindex="-1" role="dialog"
               aria-labelledby="detailInfoModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">

          <div id="detailModalBody" class="modal-body">
            <el-row v-if="showPieData.showGenderProportion != null" type="flex" justify="center">
              <el-col class="centerCol" :span="12" >
                <div class="pieChart"><PieChart :data="showPieData.showGenderProportion"
                title="Gender Proportion"/></div>
              </el-col>
              <el-col class="centerCol" :span="12">
                <div class="pieChart"><PieChart :data="showPieData.showAgeProportion"
                title="Age Proportion"/></div>
              </el-col>
            </el-row>
            <el-row v-if="showPieData.showGenderProportion != null" type="flex" justify="center">
              <el-col class="centerCol" :span="12">
                <div style="font-size: 12px; line-height: 22px">
                  <div>Total: {{populationData[curArea][curLocation].total}}</div>
                </div>
              </el-col>
              <el-col class="centerCol" :span="12">
                <div style="font-size: 12px; line-height: 22px">
                  <div>Median Age: {{populationData[curArea][curLocation].medianAge}}</div>
                </div>
              </el-col>
            </el-row>
            <div style="text-align: center; line-height: 30px" v-else>
              <div style="font-weight: bold">NO DATA</div>
              <div style="font-size: 12px">Please refer to its neighbours</div>
            </div>

            <el-row v-if="showPieData.showIncomeProportion != null">
              <el-col class="centerCol" :span="12">
                <div class="pieChart"><PieChart :data="showPieData.showIncomeProportion"
                title="Income Proportion" /></div>
              </el-col>
              <el-col class="centerCol" :span="12">
                <div class="pieChart"><PieChart :data="showPieData.showSourceProportion"
                title="Source Proportion"/></div>
              </el-col>
            </el-row>
            <el-row v-if="showPieData.showIncomeProportion != null" type="flex" justify="center">
                <div style="font-size: 12px; line-height: 22px">
                  <div>Mean total income: {{incomeData[curArea][curLocation].mean}}</div>
                  <div>Median total income: {{incomeData[curArea][curLocation].median}}</div>
                </div>
            </el-row>
            <div style="text-align: center; line-height: 30px" v-else>
              <div style="font-weight: bold">NO DATA</div>
              <div style="font-size: 12px">Please refer to its neighbours</div>
            </div>


          </div>
            <div class="modal-footer">
              <button class="btn btn-secondary btn-sm" data-dismiss="modal">Close</button>
            </div>
          </div>
      </div>
    </div>





  </div>
  

</template>

<script>
  import { create, all } from 'mathjs'
  import Common from './Common'
  import { Notification } from 'element-ui';
  import { Message } from 'element-ui';
  import Navitem from './Navitem'
  import PieChart from './PieChartComponent'
  import populationJsonAU from '../../static/AU_pop.json'
  import populationJsonMEL from '../../static/Mel_pop.json'
  import incomeJsonAU from '../../static/AU_income.json'
  import incomeJsonMEL from '../../static/Mel_income.json'
  import neighborJsonMEL from '../../static/Neighbours.json'
  import $ from 'jquery'


  export default {

    name: 'MapComponent',
    components:{
      PieChart,
      Navitem,
    },
    data(){
      return{
        curTopic: null,
        curArea: null,
        curLocation: null,
        curModal: null,
        showPieData: {
          showIncomeProportion: null,
          showSourceProportion: null,
          showGenderProportion: null,
          showAgeProportion: null,
        },
        incomeData: {
          states: {},
          mel: {}
        },
        populationData: {
          states: {},
          mel: {}
        },
        neighborList: {},
        isCollapse: true,
      }

    },
    mounted() {
      this.initMap()
      this.getAurinData()
      this.listenToResize()
      this.$root.$refs.Navitem.changeNavIndex('map');
    },
    methods: {

      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },

      initMap() {
        let map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -27, lng: 134},
          zoom: 5,
          disableDefaultUI: true
        })
      },


      getColorRank(value, lQuantile, rQuantile){
        let interval = (rQuantile - lQuantile) / 4
        if (value <= lQuantile) return 0
        else if(value > lQuantile && value <= lQuantile + interval) return 1
        else if(value > lQuantile + interval && value <= lQuantile + 2*interval) return 2
        else if(value > lQuantile + 2*interval && value <= lQuantile + 3*interval) return 3
        else if(value > lQuantile + 3*interval && value <= rQuantile) return 4
        else return 5
      },

      getAurinData() {
        const math = create(all, {})
        processPopulation(populationJsonAU, this.populationData.states, this.getColorRank)
        processPopulation(populationJsonMEL, this.populationData.mel, this.getColorRank)
        processIncome(incomeJsonAU, this.incomeData.states, this.getColorRank)
        processIncome(incomeJsonMEL, this.incomeData.mel, this.getColorRank)
        for(const key in neighborJsonMEL){
          let record = neighborJsonMEL[key]
          this.neighborList[record['name']] = record['neighbors']
        }
        function processPopulation (json, populationArea, getColorRank) {
          let sizeList = [], ageList = []
          for (const key in json) {
            let label
            let record = json[key]
            if (populationArea[record['Name']] != null) continue
            populationArea[record['Name']] = {
              maleTotal: null,
              femaleTotal: null,
              total: null,
              medianAge: null,
              ageLevel: null,
              sizeLevel: null,
              charts: {
                ageProportion: [],
                genderProportion: []
              }
            }
            let obj = populationArea[record['Name']]
            obj.maleTotal = record['Gender proportion']['Total male population']
            obj.femaleTotal = record['Gender proportion']['Total Female population']
            obj.total = obj.maleTotal + obj.femaleTotal
            sizeList.push(obj.total)
            obj.medianAge = record['Median age']
            ageList.push(obj.medianAge)
            for (label in record['Age proportion']) {
              obj.charts.ageProportion.push({name: label, value: record['Age proportion'][label]})
            }
            for (label in record['Gender proportion']) {
              obj.charts.genderProportion.push({name: label, value: record['Gender proportion'][label]})
            }
          }
          let sizeMean = math.mean(sizeList), sizeStd = math.std(sizeList)
          let lSizeQuantile = sizeMean - 2 * sizeStd, rSizeQuantile = sizeMean + 2 * sizeStd
          let ageMean = math.mean(ageList), ageStd = math.std(ageList)
          let lAgeQuantile = ageMean - 2 * ageStd, rAgeQuantile = ageMean + 2 * ageStd
          for (const key in json) {
            populationArea[json[key]['Name']].sizeLevel =
              getColorRank(populationArea[json[key]['Name']].total, lSizeQuantile, rSizeQuantile)
            populationArea[json[key]['Name']].ageLevel =
              getColorRank(populationArea[json[key]['Name']].medianAge, lAgeQuantile, rAgeQuantile)
          }
        }
        function processIncome (json, incomeArea, getColorRank) {
          let list = []
          for (const key in json) {
            let label
            let record = json[key]
            if (incomeArea[record['Name']] != null) continue
            incomeArea[record['Name']] = {
              median: null,
              mean: null,
              incomeLevel: null,
              charts: {
                incomeProportion: [],
                sourceProportion: []
              }
            }
            let obj = incomeArea[record['Name']]
            obj.median = record['Personal median total income']
            obj.mean = record['Personal mean total income']
            list.push(obj.mean)
            for (label in record['Income proportion']) {
              obj.charts.incomeProportion.push({name: label, value: record['Income proportion'][label]})
            }
            for (label in record['Main source proportion']) {
              obj.charts.sourceProportion.push({name: label, value: record['Main source proportion'][label]})
            }
          }
          let mean = math.mean(list), std = math.std(list)
          let lQuantile = mean - 2*std, rQuantile = mean + 3*std
          for (const key in json) {
            incomeArea[json[key]['Name']].incomeLevel =
              getColorRank(incomeArea[json[key]['Name']].mean, lQuantile, rQuantile)
          }
        }
      },


      changeTopic(topic) {
        if(this.curTopic !== topic){
          this.curTopic = topic
          this.curArea = null
          this.initMap()
        }
      },

      switchTo(area) {
        Common.loading("Loading...", 1000)
        this.curArea = area
        let thisObj = this
        let infoWindow = new google.maps.InfoWindow({});
        if(area === 'states'){
          let colors = ["#ffffff","#f6ebeb","#e5b1ae","#da8b86","#c95249","#b8180c"]
          let map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: -28, lng: 134},
            zoom: 4.5,
            disableDefaultUI: true
          })
          map.data.loadGeoJson(
            '../../static/AUgeo.json');
          map.data.setStyle(function(feature){
            return getColor(thisObj, colors, feature.getProperty('GCC_NAME16'))
          })

          google.maps.event.addListener(infoWindow, 'closeclick', function() {
            map.data.revertStyle();
          });

          map.data.addListener('click', function (event) {
            map.data.revertStyle();
            map.data.overrideStyle(event.feature, { strokeWeight: 1, fillColor: '#007bff', fillOpacity: 0.8});
            let name = event.feature.getProperty('GCC_NAME16')
            thisObj.showData(thisObj, name)
            thisObj.curLocation = name
            let info = '<h6>' + name + '</h6>';
            info += thisObj.createInfo(thisObj, name)
            infoWindow.setContent(info)
            infoWindow.setPosition(event.latLng);
            infoWindow.open(map)
          })

        }
        else if(area === 'mel') {
          let colors = ["#ffffff","#dbe5c6","#bed4af","#91b98d","#659f6a","#398548"]
          let map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: -38, lng: 145},
            zoom: 10.5,
            disableDefaultUI: true
          })

          map.data.loadGeoJson(
            '../../static/Melgeo.json');

          map.data.setStyle(function(feature){
            return getColor(thisObj, colors, feature.getProperty('name'))
          })

          google.maps.event.addListener(infoWindow, 'closeclick', function() {
            map.data.revertStyle();
          });

          map.data.addListener('click', function (event) {
            map.data.revertStyle();
            map.data.overrideStyle(event.feature, { strokeWeight: 1, fillColor: '#007bff', fillOpacity: 0.8});
            let name = event.feature.getProperty('name')
            thisObj.showData(thisObj, name)
            thisObj.curLocation = name
            let info = '<h6>' + name + '</h6>';
            info += thisObj.createInfo(thisObj, name)
            infoWindow.setContent(info)
            infoWindow.setPosition(event.latLng);
            infoWindow.open(map);
          })
        }

        
        function getColor (thisObj, colors, name) {
          let index = -1
          let neighbors = thisObj.neighborList[name]
          let levelMap = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}, max = 0

          function shuffling(level){
            levelMap[level] += 1
            max = (levelMap[level] > max) ?
              levelMap[level] : max
          }

          function reducing(){
            const math = create(all, {})
            let result = []
            for(const key in levelMap){
              if(levelMap[key] === max){
                result.push(key)
              }
            }
            return Math.ceil(math.mean(result))
          }

          switch(thisObj.curLabel){
            case 'size':
              if(thisObj.populationData[thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.populationData[thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.sizeLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.populationData[thisObj.curArea][name].sizeLevel
              break
            case 'age':
              if(thisObj.populationData[thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.populationData[thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.ageLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.populationData[thisObj.curArea][name].ageLevel
              break
            case 'income':
              if(thisObj.incomeData[thisObj.curArea][name] == null) {
                if(neighbors == null) break
                for(const n of neighbors){
                  let neighborData = thisObj.incomeData[thisObj.curArea][n]
                  if(neighborData == null) continue
                  shuffling(neighborData.incomeLevel)
                }
                index = (max === 0) ? -1 : reducing()
                break
              }
              index = thisObj.incomeData[thisObj.curArea][name].incomeLevel
              break
          }
          if(index === -1) return {
            fillColor: 'grey',
            fillOpacity: 0.6,
            strokeWeight: 1
          }
          else return{
            fillColor: colors[index],
            fillOpacity: 0.8,
            strokeWeight: 1
          }
        }
      },

      showData(thisObj, name){
        thisObj.showPieData.showGenderProportion = (thisObj.populationData[thisObj.curArea][name] != null) ?
          thisObj.populationData[thisObj.curArea][name].charts.genderProportion : null
        thisObj.showPieData.showAgeProportion = (thisObj.populationData[thisObj.curArea][name] != null) ?
          thisObj.populationData[thisObj.curArea][name].charts.ageProportion : null
        thisObj.showPieData.showIncomeProportion = (thisObj.incomeData[thisObj.curArea][name] != null) ?
          thisObj.incomeData[thisObj.curArea][name].charts.incomeProportion : null
        thisObj.showPieData.showSourceProportion = (thisObj.incomeData[thisObj.curArea][name] != null) ?
          thisObj.incomeData[thisObj.curArea][name].charts.sourceProportion : null
      },

      createInfo(thisObj, name){
        let topicData = null
        let info = ''
        let topicName = ''

        let err = '<div style="font-size: 12px; line-height: 22px"><div style="font-weight: bold"> NO DATA </div>' +
          '<div>Color simulated by its neighbours</div></div>'
        switch (thisObj.curLabel){
          case 'size':
            if(thisObj.populationData[thisObj.curArea][name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Total: ' + thisObj.populationData[thisObj.curArea][name].total + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> more </a></div>'
            break
          case 'age':
            if(thisObj.populationData[thisObj.curArea][name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Median Age: ' + thisObj.populationData[thisObj.curArea][name].medianAge + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> more </a></div>'
            break
          case 'income':
            if(thisObj.incomeData[thisObj.curArea][name] == null) return err
            info += '<div style="font-size: 12px; line-height: 22px"> ' +
              '<div> Mean: ' + thisObj.incomeData[thisObj.curArea][name].mean + '</div>' +
              '<div> Median: ' + thisObj.incomeData[thisObj.curArea][name].median + '</div>' +
              '<a href="#" data-toggle="modal" data-target="#detailInfoModal"> more </a></div>'
            break
        }
        return info
      },



      changeTag(tag, noWait){
        this.curModal = tag
        if(noWait == null)
          Common.loading("Initializing Charts...", 1000, document.getElementById('detailModalBody'))
      },

      listenToResize(){
        let changeTag = this.changeTag
        let loading = Common.loading
        $('#detailInfoModal').on('show.bs.modal', function () {
          loading('Initializing Charts...', 1000, document.getElementById('detailModalBody'))
          changeTag('tweets', true)
        });
        $('#detailInfoModal').on('hide.bs.modal', function () {
          changeTag(null, true)
        });
      },

      addMarkers1() {
        let map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -27, lng: 134},
          zoom: 5,
          disableDefaultUI: true
        })
        var marker = new google.maps.Marker({
            position: {
              lat: -31.9523,
              lng: 115.8613,
            },
            map: map,
        });
        var marker2 = new google.maps.Marker({
            position: {
              lat: -37.8136,
              lng: 144.9631,
            },
            map: map,
        });
        var marker3 = new google.maps.Marker({
            position: {
              lat: -33.8688,
              lng: 151.2093,
            },
            map: map,
        });
        var marker4 = new google.maps.Marker({
            position: {
              lat: -27.4705,
              lng: 153.0260,
            },
            map: map,
        });
        var marker5 = new google.maps.Marker({
            position: {
              lat: -34.9285,
              lng: 138.6007,
            },
            map: map,
        });
        var marker6 = new google.maps.Marker({
            position: {
              lat: -35.2809,
              lng: 149.1300,
            },
            map: map,
        });
        var tot = this.getTotTwitter("http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=Perth");
        var tot2 = this.getTotTwitter("http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=Melbourne");
        var tot3 = this.getTotTwitter("http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=Sydney");
        var tot4 = this.getTotTwitter("http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=Brisbane");
        var tot5 = this.getTotTwitter("http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=Adelaide");
        var tot6 = this.getTotTwitter("http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=Canberra");
        var infowindow = new google.maps.InfoWindow({
          content: '<h5>--Perth--</h5>'+"<h5>" + tot + "</h5>",
        });
        var infowindow2 = new google.maps.InfoWindow({
          content: '<h5>--Melbourne--</h5>'+"<h5>" + tot2 + "</h5>",
        });
        var infowindow3 = new google.maps.InfoWindow({
          content: '<h5>--Sydney--</h5>'+"<h5>" + tot3 + "</h5>",
        });
        var infowindow4 = new google.maps.InfoWindow({
          content: '<h5>--Brisbane--</h5>'+"<h5>" + tot4 + "</h5>",
        });
        var infowindow5 = new google.maps.InfoWindow({
          content: '<h5>--Adelaide--</h5>'+"<h5>" + tot5 + "</h5>",
        });
        var infowindow6 = new google.maps.InfoWindow({
          content: '<h5>--Canberra--</h5>'+"<h5>" + tot6 + "</h5>",
        });
        marker.addListener("mouseover", () => {
            infowindow.open(this.maps, marker);
        });
        marker2.addListener("mouseover", () => {
            infowindow2.open(this.maps, marker2);
        });
        marker3.addListener("mouseover", () => {
            infowindow3.open(this.maps, marker3);
        });
        marker4.addListener("mouseover", () => {
            infowindow4.open(this.maps, marker4);
        });
        marker5.addListener("mouseover", () => {
            infowindow5.open(this.maps, marker5);
        });
        marker6.addListener("mouseover", () => {
            infowindow6.open(this.maps, marker6);
        });
      },

      addMarkers2() {
        let map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -27, lng: 134},
          zoom: 5,
          disableDefaultUI: true
        })
        var marker = new google.maps.Marker({
            position: {
              lat: -31.9523,
              lng: 115.8613,
            },
            map: map,
        });
        var marker2 = new google.maps.Marker({
            position: {
              lat: -37.8136,
              lng: 144.9631,
            },
            map: map,
        });
        var marker3 = new google.maps.Marker({
            position: {
              lat: -33.8688,
              lng: 151.2093,
            },
            map: map,
        });
        var marker4 = new google.maps.Marker({
            position: {
              lat: -27.4705,
              lng: 153.0260,
            },
            map: map,
        });
        var marker5 = new google.maps.Marker({
            position: {
              lat: -34.9285,
              lng: 138.6007,
            },
            map: map,
        });
        var marker6 = new google.maps.Marker({
            position: {
              lat: -35.2809,
              lng: 149.1300,
            },
            map: map,
        });
        var emo = this.getEmoji("http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=Perth&start_time=0-0-0&end_time=0-0-0&module=get_feature");
        var emo2 = this.getEmoji("http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=Melbourne&start_time=0-0-0&end_time=0-0-0&module=get_feature");
        var emo3 = this.getEmoji("http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=Sydney&start_time=0-0-0&end_time=0-0-0&module=get_feature");
        var emo4 = this.getEmoji("http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=Brisbane&start_time=0-0-0&end_time=0-0-0&module=get_feature");
        var emo5 = this.getEmoji("http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=Adelaide&start_time=0-0-0&end_time=0-0-0&module=get_feature");
        var emo6 = this.getEmoji("http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=Canberra&start_time=0-0-0&end_time=0-0-0&module=get_feature");
        var infowindow = new google.maps.InfoWindow({
          content: '<h4>---Perth---</h4>'+"<h4>" + emo + "</h4>",
        });
        var infowindow2 = new google.maps.InfoWindow({
          content: '<h4>---Melbourne---</h4>'+"<h4>" + emo2 + "</h4>",
        });
        var infowindow3 = new google.maps.InfoWindow({
          content: '<h4>---Sydney---</h4>'+"<h4>" + emo3 + "</h4>",
        });
        var infowindow4 = new google.maps.InfoWindow({
          content: '<h4>---Brisbane---</h4>'+"<h4>" + emo4 + "</h4>",
        });
        var infowindow5 = new google.maps.InfoWindow({
          content: '<h4>---Adelaide---</h4>'+"<h4>" + emo5 + "</h4>",
        });
        var infowindow6 = new google.maps.InfoWindow({
          content: '<h4>---Canberra---</h4>'+"<h4>" + emo6 + "</h4>",
        });
        marker.addListener("mouseover", () => {
            infowindow.open(this.maps, marker);
        });
        marker2.addListener("mouseover", () => {
            infowindow2.open(this.maps, marker2);
        });
        marker3.addListener("mouseover", () => {
            infowindow3.open(this.maps, marker3);
        });
        marker4.addListener("mouseover", () => {
            infowindow4.open(this.maps, marker4);
        });
        marker5.addListener("mouseover", () => {
            infowindow5.open(this.maps, marker5);
        });
        marker6.addListener("mouseover", () => {
            infowindow6.open(this.maps, marker6);
        });
      },

      addMarkers3() {
        let map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -27, lng: 134},
          zoom: 5,
          disableDefaultUI: true
        })
        var marker = new google.maps.Marker({
            position: {
              lat: -31.9523,
              lng: 115.8613,
            },
            map: map,
        });
        var marker2 = new google.maps.Marker({
            position: {
              lat: -37.8136,
              lng: 144.9631,
            },
            map: map,
        });
        var marker3 = new google.maps.Marker({
            position: {
              lat: -33.8688,
              lng: 151.2093,
            },
            map: map,
        });
        var marker4 = new google.maps.Marker({
            position: {
              lat: -27.4705,
              lng: 153.0260,
            },
            map: map,
        });
        var marker5 = new google.maps.Marker({
            position: {
              lat: -34.9285,
              lng: 138.6007,
            },
            map: map,
        });
        var marker6 = new google.maps.Marker({
            position: {
              lat: -35.2809,
              lng: 149.1300,
            },
            map: map,
        });
        var tag = this.getHashtag("http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=Perth&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var tag2 = this.getHashtag("http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=Melbourne&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var tag3 = this.getHashtag("http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=Sydney&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var tag4 = this.getHashtag("http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=Brisbane&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var tag5 = this.getHashtag("http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=Adelaide&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var tag6 = this.getHashtag("http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=Canberra&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var infowindow = new google.maps.InfoWindow({
          content: '<h4>---Perth---</h4>'+
                   "<h6>#" + tag[0] + "\n</h6>"+
                   "<h6>#" + tag[1] + "\n</h6>"+
                   "<h6>#" + tag[2] + "\n</h6>"+
                   "<h6>#" + tag[3] + "\n</h6>"+
                   "<h6>#" + tag[4] + "\n</h6>",
        });
        var infowindow2 = new google.maps.InfoWindow({
          content: '<h4>---Melbourne---</h4>'+
                   "<h6>#" + tag2[0] + "\n</h6>"+
                   "<h6>#" + tag2[1] + "\n</h6>"+
                   "<h6>#" + tag2[2] + "\n</h6>"+
                   "<h6>#" + tag2[3] + "\n</h6>"+
                   "<h6>#" + tag2[4] + "\n</h6>",
        });
        var infowindow3 = new google.maps.InfoWindow({
          content: '<h4>---Sydney---</h4>'+
                   "<h6>#" + tag3[0] + "\n</h6>"+
                   "<h6>#" + tag3[1] + "\n</h6>"+
                   "<h6>#" + tag3[2] + "\n</h6>"+
                   "<h6>#" + tag3[3] + "\n</h6>"+
                   "<h6>#" + tag3[4] + "\n</h6>",
        });
        var infowindow4 = new google.maps.InfoWindow({
          content: '<h4>---Brisbane---</h4>'+
                   "<h6>#" + tag4[0] + "\n</h6>"+
                   "<h6>#" + tag4[1] + "\n</h6>"+
                   "<h6>#" + tag4[2] + "\n</h6>"+
                   "<h6>#" + tag4[3] + "\n</h6>"+
                   "<h6>#" + tag4[4] + "\n</h6>",
        });
        var infowindow5 = new google.maps.InfoWindow({
          content: '<h4>---Adelaide---</h4>'+
                   "<h6>#" + tag5[0] + "\n</h6>"+
                   "<h6>#" + tag5[1] + "\n</h6>"+
                   "<h6>#" + tag5[2] + "\n</h6>"+
                   "<h6>#" + tag5[3] + "\n</h6>"+
                   "<h6>#" + tag5[4] + "\n</h6>",
        });
        var infowindow6 = new google.maps.InfoWindow({
          content: '<h4>---Canberra---</h4>'+
                   "<h6>#" + tag6[0] + "\n</h6>"+
                   "<h6>#" + tag6[1] + "\n</h6>"+
                   "<h6>#" + tag6[2] + "\n</h6>"+
                   "<h6>#" + tag6[3] + "\n</h6>"+
                   "<h6>#" + tag6[4] + "\n</h6>",
        });
        marker.addListener("mouseover", () => {
            infowindow.open(this.maps, marker);
        });
        marker2.addListener("mouseover", () => {
            infowindow2.open(this.maps, marker2);
        });
        marker3.addListener("mouseover", () => {
            infowindow3.open(this.maps, marker3);
        });
        marker4.addListener("mouseover", () => {
            infowindow4.open(this.maps, marker4);
        });
        marker5.addListener("mouseover", () => {
            infowindow5.open(this.maps, marker5);
        });
        marker6.addListener("mouseover", () => {
            infowindow6.open(this.maps, marker6);
        });
      },

      addMarkers4() {
        let map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -27, lng: 134},
          zoom: 5,
          disableDefaultUI: true
        })
        var marker = new google.maps.Marker({
            position: {
              lat: -31.9523,
              lng: 115.8613,
            },
            map: map,
        });
        var marker2 = new google.maps.Marker({
            position: {
              lat: -37.8136,
              lng: 144.9631,
            },
            map: map,
        });
        var marker3 = new google.maps.Marker({
            position: {
              lat: -33.8688,
              lng: 151.2093,
            },
            map: map,
        });
        var marker4 = new google.maps.Marker({
            position: {
              lat: -27.4705,
              lng: 153.0260,
            },
            map: map,
        });
        var marker5 = new google.maps.Marker({
            position: {
              lat: -34.9285,
              lng: 138.6007,
            },
            map: map,
        });
        var marker6 = new google.maps.Marker({
            position: {
              lat: -35.2809,
              lng: 149.1300,
            },
            map: map,
        });
        var vw = this.getVulgar("http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=Perth&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var vw2 = this.getVulgar("http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=Melbourne&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var vw3 = this.getVulgar("http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=Sydney&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var vw4 = this.getVulgar("http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=Brisbane&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var vw5 = this.getVulgar("http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=Adelaide&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var vw6 = this.getVulgar("http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=Canberra&start_time=2021-5-0&end_time=2021-5-0&module=get_feature");
        var infowindow = new google.maps.InfoWindow({
          content: '<h4>---Perth---</h4>'+
                   "<h6>" + vw[0] + "\n</h6>"+
                   "<h6>" + vw[1] + "\n</h6>"+
                   "<h6>" + vw[2] + "\n</h6>"+
                   "<h6>" + vw[3] + "\n</h6>"+
                   "<h6>" + vw[4] + "\n</h6>",
        });
        var infowindow2 = new google.maps.InfoWindow({
          content: '<h4>---Melbourne---</h4>'+
                   "<h6>" + vw2[0] + "\n</h6>"+
                   "<h6>" + vw2[1] + "\n</h6>"+
                   "<h6>" + vw2[2] + "\n</h6>"+
                   "<h6>" + vw2[3] + "\n</h6>"+
                   "<h6>" + vw2[4] + "\n</h6>",
        });
        var infowindow3 = new google.maps.InfoWindow({
          content: '<h4>---Sydney---</h4>'+
                   "<h6>" + vw3[0] + "\n</h6>"+
                   "<h6>" + vw3[1] + "\n</h6>"+
                   "<h6>" + vw3[2] + "\n</h6>"+
                   "<h6>" + vw3[3] + "\n</h6>"+
                   "<h6>" + vw3[4] + "\n</h6>",
        });
        var infowindow4 = new google.maps.InfoWindow({
          content: '<h4>---Brisbane---</h4>'+
                   "<h6>" + vw4[0] + "\n</h6>"+
                   "<h6>" + vw4[1] + "\n</h6>"+
                   "<h6>" + vw4[2] + "\n</h6>"+
                   "<h6>" + vw4[3] + "\n</h6>"+
                   "<h6>" + vw4[4] + "\n</h6>",
        });
        var infowindow5 = new google.maps.InfoWindow({
          content: '<h4>---Adelaide---</h4>'+
                   "<h6>" + vw5[0] + "\n</h6>"+
                   "<h6>" + vw5[1] + "\n</h6>"+
                   "<h6>" + vw5[2] + "\n</h6>"+
                   "<h6>" + vw5[3] + "\n</h6>"+
                   "<h6>" + vw5[4] + "\n</h6>",
        });
        var infowindow6 = new google.maps.InfoWindow({
          content: '<h4>---Canberra---</h4>'+
                   "<h6>" + vw6[0] + "\n</h6>"+
                   "<h6>" + vw6[1] + "\n</h6>"+
                   "<h6>" + vw6[2] + "\n</h6>"+
                   "<h6>" + vw6[3] + "\n</h6>"+
                   "<h6>" + vw6[4] + "\n</h6>",
        });
        marker.addListener("mouseover", () => {
            infowindow.open(this.maps, marker);
        });
        marker2.addListener("mouseover", () => {
            infowindow2.open(this.maps, marker2);
        });
        marker3.addListener("mouseover", () => {
            infowindow3.open(this.maps, marker3);
        });
        marker4.addListener("mouseover", () => {
            infowindow4.open(this.maps, marker4);
        });
        marker5.addListener("mouseover", () => {
            infowindow5.open(this.maps, marker5);
        });
        marker6.addListener("mouseover", () => {
            infowindow6.open(this.maps, marker6);
        });
      },

      getTotTwitter(url) {
        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  },
                  'false': function (data) {
                      json = null;
                  }
              });
              return json;
        })();

        if (json_data === null)
        {
          chartDom.innerHTML = "Error on fetching data from server. Please check if you have connected to the Australia Network.";
        } else {
          var value = json_data["rows"][0].value;
          return value;         
        } 
      },

      getEmoji(url) {
        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  },
                  'false': function (data) {
                      json = null;
                  }
              });
              return json;
        })();

        if (json_data === null)
        {
          chartDom.innerHTML = "Error on fetching data from server. Please check if you have connected to the Australia Network.";
        } else {
          let data = [];
          for(let o in json_data) {
            let item = {value: json_data[o], name: o};
            data.push(item);         
          }
          data.sort(function(a, b) {
            return b.value - a.value;
          }); 
          var arr = [data[0].name,data[1].name,data[2].name,data[3].name,data[4].name];
          return arr;
        }
      },

      getHashtag(url) {
        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  },
                  'false': function (data) {
                      json = null;
                  }
              });
              return json;
        })();

        if (json_data === null)
        {
          chartDom.innerHTML = "Error on fetching data from server. Please check if you have connected to the Australia Network.";
        } else {
          let data = [];
          for(let o in json_data) {
            let item = {value: json_data[o], name: o};
            data.push(item);         
          }
          data.sort(function(a, b) {
            return b.value - a.value;
          }); 
          var arr = [data[0].name,data[1].name,data[2].name,data[3].name,data[4].name];
          return arr;
        }
      },

      getVulgar(url) {
        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  },
                  'false': function (data) {
                      json = null;
                  }
              });
              return json;
        })();

        if (json_data === null)
        {
          chartDom.innerHTML = "Error on fetching data from server. Please check if you have connected to the Australia Network.";
        } else {
          let data = [];
          for(let o in json_data) {
            let item = {value: json_data[o], name: o};
            data.push(item);         
          }
          data.sort(function(a, b) {
            return b.value - a.value;
          }); 
          var arr = [data[0].name,data[1].name,data[2].name,data[3].name,data[4].name];
          return arr;
        }
      }
    }
  }

</script>

<style>
  #map {
    height: 100vh;
    width: 100%
  }

  #clickables {
    position: absolute;
    width: 100%;
    top: 90px;
    margin-top: 75px;
  }

  #detailInfoModal {
    position: absolute;
    top: 50%; left: 50%;
    width: 30%;
    transform: translate(-50%,-50%);
  }

  .separator {
    padding: 0.25rem 1.5rem;
    font-weight: 500;
  }

  .dropdown-menu{
    background-color: #1d2124;
    color: white;
  }

  .dropdown-item{
    cursor: pointer;
    background-color: #1d2124;
  }

  .dropdown-item:hover{
    background-color:#007bff
  }

  .pieChart {
    height: 150px;
    width: 150px;
  }

  .centerCol {
    display:flex;
    justify-content:center;
    align-items:center;
  }

  #detailModalBody .el-loading-spinner {
    transform: translate(-50%, 0);
  }

  #detailModalBody .el-loading-spinner .el-loading-text {
    font-size: 12px;
  }

</style>
