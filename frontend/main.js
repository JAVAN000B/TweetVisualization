var Main = {
  data() {
    return {
      // activeIndex: '1',
      // activeIndex2: '1',
      fits: ['contain'],
      url: 'images/web_icon.jpg',
      items: ["Explore the world", "Examine our data map", "How many tweets are you producing everyday", "Enjoy the beauty of technology"]
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
var Ctor = Vue.extend(Main)
new Ctor().$mount('#app')
