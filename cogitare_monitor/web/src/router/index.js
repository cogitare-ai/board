import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Config from '@/components/Config'
import Viewer from '@/components/Viewer'

Vue.use(Router)

export const router = new Router({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Index
        },
        {
            path: '/config',
            name: 'Configuration',
            component: Config
        },
        {
            path: '/view/:id',
            name: 'Viewer',
            component: Viewer
        }
    ]
})
