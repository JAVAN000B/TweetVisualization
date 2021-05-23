<template>
  <div>
    <Navitem class="bar"/>
    <div id="background">
      <div id="clickables">
        <el-row>
          <el-col>
            <el-cascader
              v-model="value"
              :options="options"
              @change="handleChange"
              placeholder="Select Graph"
              clearable
              :show-all-levels="false"
              style='width: 300px'>
            </el-cascader>
          </el-col>
        </el-row>
        <div id="main"></div>
      </div>
    </div>   
  </div>

</template>

<script>
  import Navitem from './Navitem'
  import echarts from 'echarts'
  import $ from 'jquery'
  import 'echarts-wordcloud';

  export default {
    components: {
      Navitem,
    },

    data(){
      return {
        value: [],
        options: [{
          value: 'states_bar_chart',
          label: 'States Data Charts',
          children: [{
            value: 'au_population',
            label: 'AU Population Bar Chart',
            }, {
            value: 'au_gender',
            label: 'AU Gender Bar Chart',
            }, {
            value: 'au_age',
            label: 'AU Age Bar Chart',
            }, {
            value: 'au_income',
            label: 'AU Income Bar Chart',
            }, {
            value: 'vic_population_distribution',
            label: 'Victoria Population Distribution',
            }]
          },
          {
            value: 'melb_pie_chart',
            label: 'Melbourne Data Charts',
            children: [{
            value: 'melb_population',
            label: 'Melbourne Population Pie Chart',
            }, {
            value: 'melb_gender',
            label: 'Melbourne Gender Pie Chart',
            }, {
            value: 'melb_age',
            label: 'Melbourne Age Pie Chart',
            }, {
            value: 'melb_income',
            label: 'Melbourne Income Pie Chart',
            }]
          },
          {
            value: 'twitter_pie_chart',
            label: 'Twitter Pie Charts',
            children: [{
            value: 'au_emoji_pie_chart',
            label: 'AU Emoji Pie Chart',
            }, {
            value: 'au_hashtag_pie_chart',
            label: 'AU Hashtag Pie Chart',
            }, {
            value: 'au_vulgar_word_pie_chart',
            label: 'AU Vulgar Word Pie Chart', 
            }, {
            value: 'au_tweets_pie_chart',
            label: 'AU State Tweets Pie Chart', 
            }, {
            value: 'city_tweets_pie_chart',
            label: 'AU City Tweets Pie Chart', 
            }, {
            value: 'city_life_pie_chart',
            label: 'AU City Life Pie Chart', 
            children: [{
              value: 'Melbourne',
              label: 'Melbourne',
              },
              {
              value: 'Sydney',
              label: 'Sydney',
              },
              {
              value: 'Canberra',
              label: 'Canberra',
              },
              {
              value: 'Brisbane',
              label: 'Brisbane',
              },
              {
              value: 'Hobart',
              label: 'Hobart',
              },
              {
              value: 'Perth',
              label: 'Perth',
              },
              {
              value: 'Adelaide',
              label: 'Adelaide',
            }],
          }]
          }, 
          {
            value: 'twitter_word_cloud',
            label: 'Twitter Word Cloud',
            children: [
              {
                value: 'au_emoji_wc',
                label: 'AU Emoji Word Cloud',
              },
              {
                value: 'au_vulgar_wc',
                label: 'AU Vulgar Word Cloud',
              },
              {
                value: 'au_hashtag_wc',
                label: 'AU Hashtag Word Cloud',
              },
              {
                value: 'au_city_emoji_wc',
                label: 'AU City Emoji Word Cloud',
                children: [{
                  value: 'Melbourne',
                  label: 'Melbourne',
                  },
                  {
                  value: 'Sydney',
                  label: 'Sydney',
                  },
                  {
                  value: 'Canberra',
                  label: 'Canberra',
                  },
                  {
                  value: 'Brisbane',
                  label: 'Brisbane',
                  },
                  {
                  value: 'Hobart',
                  label: 'Hobart',
                  },
                  {
                  value: 'Perth',
                  label: 'Perth',
                  },
                  {
                  value: 'Adelaide',
                  label: 'Adelaide',
                }],
              },
              {
                value: 'au_city_vulgar_wc',
                label: 'AU City Vulgar Word Cloud',
                children: [{
                  value: 'Melbourne',
                  label: 'Melbourne',
                  },
                  {
                  value: 'Sydney',
                  label: 'Sydney',
                  },
                  {
                  value: 'Canberra',
                  label: 'Canberra',
                  },
                  {
                  value: 'Brisbane',
                  label: 'Brisbane',
                  },
                  {
                  value: 'Hobart',
                  label: 'Hobart',
                  },
                  {
                  value: 'Perth',
                  label: 'Perth',
                  },
                  {
                  value: 'Adelaide',
                  label: 'Adelaide',
                }],
              },
              {
                value: 'au_city_hashtag_wc',
                label: 'AU City Hashtag Word Cloud',
                children: [{
                  value: 'Melbourne',
                  label: 'Melbourne',
                  },
                  {
                  value: 'Sydney',
                  label: 'Sydney',
                  },
                  {
                  value: 'Canberra',
                  label: 'Canberra',
                  },
                  {
                  value: 'Brisbane',
                  label: 'Brisbane',
                  },
                  {
                  value: 'Hobart',
                  label: 'Hobart',
                  },
                  {
                  value: 'Perth',
                  label: 'Perth',
                  },
                  {
                  value: 'Adelaide',
                  label: 'Adelaide',
                }],
              },
            ]
          },
          {
            value: 'twitter_line_chart',
            label: 'Twitter Line Chart',
            children: [{
              value: "au_states_vulgar",
              label: "AU States Vulgar Line Chart",
              children: [{
                  value: 'Australian Capital Territory',
                  label: 'Australian Capital Territory',
                  },
                  {
                  value: 'New South Wales',
                  label: 'New South Wales',
                  },
                  {
                  value: 'Queensland',
                  label: 'Queensland',
                  },
                  {
                  value: 'South Australia',
                  label: 'South Australia',
                  },
                  {
                  value: 'Victoria',
                  label: 'Victoria',
                  },
                  {
                  value: 'Western Australia',
                  label: 'Western Australia',
                }],
            },
            {
              value: "au_tweets_line",
              label: "AU Tweets Line Chart",
            },
            ]
          }
          
          ],
      }
    },

    mounted() {
      this.$root.$refs.Navitem.changeNavIndex('analysis');
    },

    methods: {
      init_bar_chart(url, index, y_name, title) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  }
              });
              return json;
        })(); 

        let x_labels = [];
        let data = [];
        for(let i = 0; i < json_data.length; i++) {
            let obj = json_data[i];
            x_labels.push(obj["Location"]);
            data.push(Number(obj[index]))
        }

        let option = this.getRegularBarChartOption(data, x_labels, y_name, title);
        option && myChart.setOption(option);
      },

      init_bar_chart_2(url, indexes, legends, title) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  }
              });
              return json;
        })(); 

        let y_labels = [];
        let datas = [[], []];
        for(let i = 0; i < json_data.length; i++) {
            let obj = json_data[i];
            y_labels.push(obj["Location"]);
            datas[0].push(Number(obj[indexes[0]]));
            datas[1].push(Number(obj[indexes[1]]));
        }

        let option = this.getTwoColumnBarChartOption(datas, title, legends, y_labels);
        option && myChart.setOption(option);
      },

      getRegularBarChartOption(data, x_labels, y_name, title) {
        let option = {
          title: {
              text: title,
              left: 'center'
          },
          tooltip: {
              trigger: 'axis',
              axisPointer: {            
                  type: 'shadow'       
              }
          },
          grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
          },
          xAxis: [
              {
                  type: 'category',
                  data: x_labels,
                  axisLabel: {  
                    interval:0,  
                    rotate:40  
                  } 
              }
          ],
          yAxis: [
              {
                  type: 'value'
              }
          ],
          series: [
              {
                  name: y_name,
                  type: 'bar',
                  barWidth: '60%',
                  data: data,
              }
          ]
        };
        return option;
      },

      getTwoColumnBarChartOption(datas, title, legends, y_labels) {
        let option = {
          title: {
              text: title,
          },
          tooltip: {
              trigger: 'axis',
              axisPointer: {
                  type: 'shadow'
              }
          },
          legend: {
              data: legends,
          },
          grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
          },
          xAxis: {
              type: 'value',
              boundaryGap: [0, 0.01]
          },
          yAxis: {
              type: 'category',
              data: y_labels,
          },
          series: [
              {
                  name: legends[0],
                  type: 'bar',
                  data: datas[0],
              },
              {
                  name: legends[1],
                  type: 'bar',
                  data: datas[1],
              }
          ]
        };
        return option;
      },

      init_pie_chart(url, indexes, title) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  }
              });
              return json;
        })(); 

        let legends = [];
        let datas = [[], []];
        for(let i = 0; i < json_data.length; i++) {
          let obj = json_data[i];
          if (obj["Location"] === indexes[0]) {
            for (let ap in obj["Age proportion"]) {
              legends.push(ap);
              let proportion = {value: obj["Age proportion"][ap], name: ap};
              datas[0].push(proportion);
            }
          } else if (obj["Location"] === indexes[1]) {
            for (let ap in obj["Age proportion"]) {
              let proportion = {value: obj["Age proportion"][ap], name: ap};
              datas[1].push(proportion);
            }
          }
        }

        let option = this.getTwoRosePieChartOption(datas, title, legends, indexes);
        option && myChart.setOption(option);
      },

      init_pie_chart_2(url, index, title, data_name) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  }
              });
              return json;
        })();

        let data = [];
        for(let i = 0; i < json_data.length; i++) {
          let obj = json_data[i];
          let item = {value: obj[index], name: obj["Location"]};
          data.push(item);
        }

        data.sort(function(a, b) {
          return b.value - a.value;
        });

        let top_20_data = data.slice(0, 20);

        let option = this.getRegularPieChartOption(top_20_data, title, data_name);
        option && myChart.setOption(option);
      },

      init_pie_chart_3(url, indexes, titles, data_names) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

        let json_data = (function() {
          let json = null;
              $.ajax({
                  'async': false,
                  'global': false,
                  'url': url,
                  'dataType': "json",
                  'success': function (data) {
                      json = data;
                  }
              });
              return json;
        })();

        let datas = [[], []];
        for(let i = 0; i < json_data.length; i++) {
          let obj = json_data[i];
          let item_0 = {value: obj[indexes[0]], name: obj["Location"]};
          let item_1 = {value: obj[indexes[1]], name: obj["Location"]};
          datas[0].push(item_0);
          datas[1].push(item_1);
        }

        for(let i = 0; i < datas.length; i++) {
          let data = datas[i];
          data.sort(function(a, b) {
            return b.value - a.value;
          });
          datas[i] = data.slice(0, 20);
        }

        let option = this.getTwoRegularPieChartOption(datas, titles, data_names);
        option && myChart.setOption(option);
      },


      getTwoRosePieChartOption(datas, title, legends, data_names) {
        let option = {
          title: {
              text: title,
              left: 'center'
          },
          tooltip: {
              trigger: 'item',
              formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
              left: 'center',
              top: 'bottom',
              data: legends,
          },
          toolbox: {
              show: true,
              feature: {
                  mark: {show: true},
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          series: [
              {
                  name: data_names[0],
                  type: 'pie',
                  radius: [20, 140],
                  center: ['25%', '50%'],
                  roseType: 'radius',
                  itemStyle: {
                      borderRadius: 5
                  },
                  emphasis: {
                      label: {
                          show: true
                      }
                  },
                  data: datas[0],
              },
              {
                  name: data_names[1],
                  type: 'pie',
                  radius: [20, 140],
                  center: ['75%', '50%'],
                  roseType: 'area',
                  itemStyle: {
                      borderRadius: 5
                  },
                  data: datas[1],
              }
          ]
        };
        return option;
      },

      getRegularPieChartOption(data, title, data_name) {
        let option = {
          title: {
              text: title,
              left: 'center'
          },
          tooltip: {
              trigger: 'item'
          },
          legend: {
              orient: 'vertical',
              left: 'left',
          },
          series: [
              {
                name: data_name,
                type: 'pie',
                radius: '50%',
                data: data,
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
              }
          ]
        };
        return option;
      },

      getBiggerRegularPieChartOption(data, title, data_name) {
        let option = {
          title: {
              text: title,
              left: 'center'
          },
          tooltip: {
              trigger: 'item'
          },
          legend: {
              orient: 'vertical',
              left: 'left',
              textStyle: {
                fontSize: '25',
              },
          },
          series: [
              {
                name: data_name,
                type: 'pie',
                radius: '50%',
                data: data,
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                label: {
                  textStyle: {
                    fontSize: '35',
                  },
                }
              }
          ]
        };
        return option;
      },

      getTwoRegularPieChartOption(datas, titles, data_names) {
        let option = {
          title: [{
            text: titles[0],
            left: '25%',
            textAlign: 'center',
          }, {
            text: titles[1],
            left: '75%',
            textAlign: 'center',
          },],
          tooltip: {
            trigger: 'item'
          },
          legend: {
            left: 'center',
            top: 'bottom',
          },
          series: [
              {
                name: data_names[0],
                type: 'pie',
                radius: '50%',
                data: datas[0],
                center: ['25%', '50%'],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
              },
              {
                name: data_names[1],
                type: 'pie',
                radius: '50%',
                data: datas[1],
                center: ['75%', '50%'],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
              }
          ]
        };
        return option;
      },

      init_twitter_chart(url, title, data_name, mode) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

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

          if (mode === 0) {
            let option = this.getRegularPieChartOption(data, title, data_name);
            option && myChart.setOption(option);
          } else {
            let option = this.getBiggerRegularPieChartOption(data, title, data_name);
            option && myChart.setOption(option);
          }
          
        } 
      },

      init_twitter_chart_2(url, title, data_name) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

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
          let json_list = json_data["rows"];
          for(let i = 0; i < json_list.length; i++) {
            let o = json_list[i];
            let item = {value: Number(o["value"]), name: String(o["key"])};
            data.push(item);
          }

          data.sort(function(a, b) {
            return b.value - a.value;
          });

          if (data.length > 15) {
            data = data.slice(0, 20);
          }

          let option = this.getRegularPieChartOption(data, title, data_name);
          option && myChart.setOption(option);
        } 
      },

      init_twitter_chart_3(urls, titles, data_names) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();
        let json_datas = [];

        for (let i = 0; i < urls.length; i++) {
          let url = urls[i];
          let j_item = (function() {
            let json = null;
                $.ajax({
                    'async': false,
                    'global': false,
                    'url': url,
                    'dataType': "json",
                    'success': function (data) {
                        json = data;
                    }
                });
                return json;
          })();
          json_datas.push(j_item);
        }

        if (json_datas.length < 3) {
          chartDom.innerHTML = "Error on fetching data from server. Please check if you have connected to the Australia Network.";
        } else {
          
          let chart_data = [];
          for (let i = 0; i < json_datas.length; i++) {
            let json_data = json_datas[i];
            let cd = [];
            for (let o in json_data) {
              cd.push({value: json_data[o], name: o});
            }
            cd.sort(function(a, b) {
              return b.value - a.value;
            });
            chart_data.push(cd);
          }

          let option = this.getCombinedPieChartOption(chart_data, titles, data_names);
          option && myChart.setOption(option);
        }
      },

      getCombinedPieChartOption(datas, titles, data_names) {
        let option = {
          title: [{
            text: titles[0],
            left: '15%',
            textAlign: 'center',
          }, {
            text: titles[1],
            left: '45%',
            textAlign: 'center',
          }, {
            text: titles[2],
            left: '82%',
            textAlign: 'center',
          },],
          tooltip: {
            trigger: 'item'
          },
          legend: {
            left: 'center',
            top: 'bottom',
          },
          series: [
              {
                name: data_names[0],
                type: 'pie',
                radius: '50%',
                data: datas[0],
                center: ['15%', '50%'],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                label: {
                  textStyle: {
                    fontSize: '20',
                  },
                }
              },
              {
                name: data_names[1],
                type: 'pie',
                radius: '50%',
                data: datas[1],
                center: ['45%', '50%'],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                label: {
                  textStyle: {
                    fontSize: '15',
                  },
                }
              },
              {
                name: data_names[2],
                type: 'pie',
                radius: '50%',
                data: datas[2],
                center: ['80%', '50%'],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                label: {
                  textStyle: {
                    fontSize: '13',
                  },
                }
              }, 
          ]
        };
        return option;
      },

      getWordCloudOption(data, title, sizeRange) {
        let option = {
          tooltip: {},
          title : {
            text: title,
            left: "center",
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          series: [ {
            type: 'wordCloud',
            gridSize: 3,
            sizeRange: sizeRange,
            rotationRange: [-45, 45],
            shape: 'pentagon',
            width: 600,
            height: 400,
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                },
            },
            data: data,
          } 
          ]
        };

        return option;
      },

      drawWorldCloud(url, title, sizeRange) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

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
                  },
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

          let option = this.getWordCloudOption(data, title, sizeRange);
          option && myChart.setOption(option);
          
        }
      },

      getLineChartOption(dateList, valueList, maxV, title) {
        let option = {

          visualMap: [{
              show: false,
              type: 'continuous',
              min: 0,
              max: maxV,
          }],


          title: [{
              left: 'center',
              text: title,
          }],
          tooltip: {
              trigger: 'axis'
          },
          xAxis: [{
              data: dateList
          }],
          yAxis: [{
          }],
          series: [{
              type: 'line',
              showSymbol: false,
              data: valueList,
              areaStyle: {}
          }]
        };
        return option;
      },

      drawLineChart(urls, start_times, title) {
        let chartDom = document.getElementById('main');
        let myChart = echarts.init(chartDom);
        myChart.clear();

        let json_datas = [];

        for (let i = 0; i < urls.length; i++) {
          let url = urls[i];
          let j_item = (function() {
            let json = null;
                $.ajax({
                    'async': false,
                    'global': false,
                    'url': url,
                    'dataType': "json",
                    'success': function (data) {
                        json = data;
                    },
                });
                return json;
          })();
          json_datas.push(j_item);
        }

        if (json_datas.length === 0)
        {
          chartDom.innerHTML = "Error on fetching data from server. Please check if you have connected to the Australia Network.";
        } else {
          let datelist = [];
          let valuelist = [];
          let maxV = 0;
          for (let i = 0; i < json_datas.length; i++) {
            let json_data = json_datas[i];
            let sum = 0;
            for (let o in json_data) {
              sum += json_data[o];
            }
            if (sum > maxV) {
              maxV = sum;
            }
            datelist.push(start_times[i]);
            valuelist.push(sum);
          }

          let option = this.getLineChartOption(datelist, valuelist, maxV, title);
          option && myChart.setOption(option);
          
        }
      },

      handleChange(value) {
        let url_1 = "../../static/aurin/result_au_income.json";
        let url_2 = "../../static/aurin/result_au_population.json";
        let url_3 = "../../static/aurin/result_melb_income.json";
        let url_4 = "../../static/aurin/result_melb_population.json";
        let au_emoji_url = "http://172.26.130.255:8001/couchdb/view/emojis/state/total?place_name=all&start_time=2021-5-0&end_time=2021-5-0&module=get_feature";
        let au_hashtag_url = "http://172.26.130.255:8001/couchdb/view/hashtag/state/total?place_name=all&start_time=2021-5-0&end_time=2021-5-0&module=get_feature";
        let au_vulgar_url = "http://172.26.130.255:8001/couchdb/view/vulgar_word/state/total?place_name=all&start_time=2021-5-0&end_time=2021-5-0&module=get_feature";
        let au_tweets_url = "http://172.26.130.255:8001/couchdb/view/num_tweet_state/?state_name=all";
        let city_tweets_url = "http://172.26.130.255:8001/couchdb/view/num_tweet_city/?city_name=all";

        if (value[0] === "states_bar_chart") {
          if (value[1] === "au_population") {
            this.init_bar_chart(url_2, "Total population", "Population", "AU Population Bar Chart");
          } else if (value[1] === "au_gender") {
            this.init_bar_chart_2(url_2, ["Total male", "Total female"], ["Male", "Female"], "AU Gender Bar Chart");
          } else if (value[1] === "au_income") {
            this.init_bar_chart_2(url_1, ["Personal mean total income", "Personal median total income"], ['Mean Personal Income', "Median Personal Income"], "AU Income Bar Chart");
          } else if (value[1] === "au_age") {
            this.init_bar_chart(url_2, "Median age", 'Median Age', "AU Age Bar Chart");
          } else {
            this.init_pie_chart(url_2, ["Rest of Vic.", "Greater Melbourne"], "Victoria Population Distribution")
          }
        } else if (value[0] === "melb_pie_chart") {
          if (value[1] === "melb_population") {
            this.init_pie_chart_2(url_4, "Total population", "Melbourne Top 20 Surburb Population Pie Chart", "Population");
          } else if (value[1] === "melb_gender") {
            this.init_pie_chart_3(url_4, ["Total male", "Total female"], ["Melbourne Top 20 Surburb Male Count Pie Chart", "Melbourne Top 20 Surburb Female Count Pie Chart"], ["Male", "Female"]);
          } else if (value[1] === "melb_age") {
            this.init_pie_chart_2(url_4, "Median age", "Melbourne Top 20 Surburb Age Pie Chart", "Median Age");
          } else if (value[1] === "melb_income") {
            this.init_pie_chart_2(url_3, "Personal mean total income", "Melbourne Top 20 Surburb Income Pie Chart", "Mean Personal Income");
          }
        } else if (value[0] === "twitter_pie_chart") {
          if (value[1] === "au_emoji_pie_chart") {
            this.init_twitter_chart(au_emoji_url, "AU Top 15 Emoji Pie Chart", "Emoji", 1);
          } else if (value[1] === "au_hashtag_pie_chart") {
            this.init_twitter_chart(au_hashtag_url, "AU Top 15 Hashtag Pie Chart", "Hashtag", 0);
          } else if (value[1] === "au_vulgar_word_pie_chart") {
            this.init_twitter_chart(au_vulgar_url, "AU Top 15 Vulgar Word Pie Chart", "Vulgar word", 0);
          } else if (value[1] === "au_tweets_pie_chart") {
            this.init_twitter_chart_2(au_tweets_url, "AU Tweets Pie Charts", "Tweets");
          } else if (value[1] === "city_tweets_pie_chart") {
            this.init_twitter_chart_2(city_tweets_url, "AU Top 20 City Tweets Pie Charts", "Tweets");
          } else {
            let city = value[2];
            let urls = ["http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=" + city + "&start_time=2021-5-0&end_time=2021-5-0&module=get_feature", "http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=" + city + "&start_time=2021-5-0&end_time=2021-5-0&module=get_feature", "http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=" + city + "&start_time=2021-5-0&end_time=2021-5-0&module=get_feature"];
            let titles = [city + " Top 15 Emoji", city + " Top 15 Vulgar Word", city + " Top 15 Hashtag"];
            let data_names = ["Emoji", "Vulgar Word", "Hashtag"];
            this.init_twitter_chart_3(urls, titles, data_names);
          }
        } else if (value[0] === "twitter_word_cloud") {
          if (value[1] === "au_emoji_wc") {
            this.drawWorldCloud(au_emoji_url, "AU Top 15 Emoji Word Cloud", [60, 220]);
          } else if (value[1] === "au_vulgar_wc") {
            this.drawWorldCloud(au_vulgar_url, "AU Top 15  Vulgar Word Cloud", [30, 110]);
          } else if (value[1] === "au_hashtag_wc") {
            this.drawWorldCloud(au_hashtag_url, "AU Top 15  Hashtag Word Cloud", [30, 110]);
          } else if (value[1] === "au_city_emoji_wc") {
            let city = value[2];
            let url = "http://172.26.130.255:8001/couchdb/view/emojis/city/total?place_name=" + city + "&start_time=2021-5-0&end_time=2021-5-0&module=get_feature";
            this.drawWorldCloud(url, city + " Top 15 Emoji Word Cloud", [60, 220]);
          } else if (value[1] === "au_city_vulgar_wc") {
            let city = value[2];
            let url = "http://172.26.130.255:8001/couchdb/view/vulgar_word/city/total?place_name=" + city + "&start_time=2021-5-0&end_time=2021-5-0&module=get_feature";
            this.drawWorldCloud(url, city + " Top 15 Vulgar Word Cloud", [30, 110]);
          } else {
            let city = value[2];
            let url = "http://172.26.130.255:8001/couchdb/view/hashtag/city/total?place_name=" + city + "&start_time=2021-5-0&end_time=2021-5-0&module=get_feature";
            this.drawWorldCloud(url, city + " Top 15 Hashtag Word Cloud", [30, 110]);
          }
        } else if (value[0] === "twitter_line_chart") {
          if (value[1] == "au_states_vulgar") {
            let start_times = [];
            let start_day = 16;
            let today = new Date();
            let dd = String(today.getDate());
            let urls = [];
            let state = value[2];
            for (let i = start_day; i <= dd; i++) {
              urls.push("http://172.26.130.255:8001/couchdb/view/vulgar_word/state/total?place_name=" + state + "&start_time=2021-5-"+ i + "&end_time=2021-5-"+ i +"&module=get_feature");
              start_times.push("2021-5-" + i);
            }
            this.drawLineChart(urls, start_times, state + " Vulgar Day Counts Line Chart");
          } else if (value[1] == "au_tweets_line") {
            let start_times = [];
            let start_day = 16;
            let today = new Date();
            let dd = String(today.getDate());
            let urls = [];
            for (let i = start_day; i <= dd; i++) {
              urls.push("http://172.26.130.255:8001/couchdb/view/total_time/?start_time=2021-5-" + i + "&end_time=2021-5-" + i);
              start_times.push("2021-5-" + i);
            }
            this.drawLineChart(urls, start_times, "AU Tweets Day Counts Line Chart");
          }
        } else {
          let chartDom = document.getElementById('main');
          let myChart = echarts.init(chartDom);
          myChart.clear();
        }
      },
    }
  };


</script>


<style>
  #background{
    position:fixed;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    margin-top: 75px;
    background-color: rgb(235, 226, 226);
  }

  #clickables {
    position: absolute;
    width: 100%;
    top: 20px;
    padding: 10px;
  }

  #main {
    width: 100%;
    height: 600px;
    background-color:whitesmoke;
    margin: 0 auto;
  }


</style>
