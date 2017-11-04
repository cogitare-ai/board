<template>
    <div class='cogitare-navbar'>
        <b-navbar toggleable="md" type="dark" variant="dark">
            <b-nav-toggle target="nav_collapse"></b-nav-toggle>
            <b-navbar-brand href="#/">
                <img id='img-logo' src='/static/logo-line.png'>
            </b-navbar-brand>

            <b-collapse is-nav id='nav_collapse'>
                <b-nav is-nav-bar>
                    <b-nav-item href="http://docs.cogitare-ai.org/" target="_blank">Docs</b-nav-item>
                    <b-nav-item href="http://github.com/cogitare-ai/cogitare" target="_blank">Github</b-nav-item>
                    <b-nav-item href="http://github.com/cogitare-ai/monitor-plugins" target="_blank">Plugins</b-nav-item>
                </b-nav>

                <b-nav is-nav-bar class="ml-auto">
                    <b-nav-item-dropdown text="Execution" right>
                        <b-dropdown-item v-for='execution in $store.state.executions' :key='execution.id'
                                         :href="'#/view/' + execution.id">
                            <div v-bind:class='"execution-status-icon " + (execution.connected == true ? "on" : "")'>
                                <icon class='icon' name='circle'></icon> {{execution.name}}
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item v-if='Object.keys($store.state.executions).length == 0'>Not connected with any execution</b-dropdown-item>
                    </b-nav-item-dropdown>

                    <b-nav-item href="#/config"><icon name="gears"></icon></b-nav-item>
                </b-nav>
            </b-collapse>
       </b-navbar>
    </div>
</template>

<script>
import 'vue-awesome/icons/gears'
import 'vue-awesome/icons/circle'
import 'vue-awesome/icons/eye'
import Icon from 'vue-awesome/components/Icon'

export default {
    name: 'cogitare-navbar',
    components: {
        Icon
    }
}
</script>

<style>
nav.navbar {
    padding: 0px;
}

#img-logo {
    max-height: 40px;
}
.execution-status-icon .icon{
    vertical-align: middle;
}
.execution-status-icon.on .icon{
    color: green;
}
</style>
