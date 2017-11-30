// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'
import { router } from './router'
import VueSocketIO from 'vue-socket.io'
import notify from './notify.js'
import Vuex from 'vuex'
import script2 from 'vue-script2'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export const MONITOR_HOST = 'http://0.0.0.0:8787'

Vue.use(Vuex)
Vue.use(script2)

const store = new Vuex.Store({
    state: {
        connected: false,
        host: null,
        executions: {}
    },

    mutations: {
        SOCKET_CONNECT: function (state, status) {
            state.connected = true
        },

        SOCKET_DISCONNECT: function (state, status) {
            state.connected = false
        },

        SOCKET_ADD_EXECUTION: function (state, data) {
            Vue.set(state.executions, data.id, data)

            window.notify.showInfo('Execution', data.name + ' connected.', function () {
                router.push({path: `view/${data.id}`})
            })
        },

        SOCKET_DISCONNECT_EXECUTION: function (state, id) {
            var name = state.executions[id].name
            state.executions[id].connected = false
            window.notify.showInfo('Execution', name + ' disconnected.')
        },

        SOCKET_REMOVE_EXECUTION: function (state, id) {
            Vue.delete(state.executions, id)
        },

        SOCKET_UPDATE_MACHINE: function (state, data) {
            var id = data['id']
            var machine = data['machine']

            Vue.set(state.executions[id], 'machine', machine)
        },

        SOCKET_ADD_USAGE_PLOT: function (state, plot) {
            Vue.set(state.executions[plot.id]._plots, plot.name, plot)
        },

        setHost: function (state, host) {
            state.host = host
        }
    },

    getters: {
        currentExecution: function (state) {
            var id = router.app.$route.params.id

            if (id in state.executions) {
                return state.executions[id]
            }
            return {}
        }
    }
})

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueSocketIO, MONITOR_HOST + '/monitor', store)
store.commit('setHost', MONITOR_HOST)
window.notify = notify

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    template: '<App/>',
    store,
    components: {
        App
    }
})
