<template>
    <div id="app">
        <cogitare-navbar></cogitare-navbar>
        <b-alert show variant="danger" v-if='!$store.state.connected'>
            Failed to connect with the Monitor Backend. Please, check if it's
            running at {{$store.state.host}}.
        </b-alert>
        <router-view/>
    </div>
</template>

<script>
import navbar from './components/cogitare-navbar.vue'

export default {
    name: 'app',
    components: {
        'cogitare-navbar': navbar
    }
}
</script>

<style>
.toast-top-right {
    top: 60px;
}
</style>
