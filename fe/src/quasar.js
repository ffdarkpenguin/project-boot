import Vue from "vue"

import "./styles/quasar.styl"
import lang from "quasar/lang/pt-br.js"
import "@quasar/extras/material-icons/material-icons.css"
import "@quasar/extras/fontawesome-v5/fontawesome-v5.css"
import {
  Quasar,
  QLayout,
  QHeader,
  QDrawer,
  QPageContainer,
  QPage,
  QToolbar,
  QToolbarTitle,
  QBtn,
  QIcon,
  QList,
  QItem,
  QItemSection,
  QItemLabel
} from "quasar"

Vue.use(Quasar, {
  config: {},
  components: {
    QLayout,
    QHeader,
    QDrawer,
    QPageContainer,
    QPage,
    QToolbar,
    QToolbarTitle,
    QBtn,
    QIcon,
    QList,
    QItem,
    QItemSection,
    QItemLabel
  },
  directives: {},
  plugins: {},
  lang: lang
})
