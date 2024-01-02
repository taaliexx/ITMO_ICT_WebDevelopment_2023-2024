const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "@/assets/variables.scss";`, // Если у вас есть файл с переменными
      },
    },
  },
  transpileDependencies: ['vuetify'], // Указывайте зависимости, которые должны быть транспилированы Babel
})
