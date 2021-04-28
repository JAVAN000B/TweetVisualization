var Main = {
  data() {
    return {
      fits: ['contain'],
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
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
