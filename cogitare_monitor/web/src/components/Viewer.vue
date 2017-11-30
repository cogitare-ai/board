<template>
    <div id='cogitare-viewer'>
        <b-alert v-if='execution.connected === false' variant="warning" show dismissible>This Execution is currently not connected. This page contains the last data from the model execution.</b-alert>
        <b-card no-body>
            <b-tabs small ref="tabs" card>
                <b-tab title="System Details" active>
                    <system-details :execution='execution'></system-details>
                </b-tab>
                <b-tab title="System Usage">
                    <system-usage :execution='execution'></system-usage>
                </b-tab>
                <b-tab title="General Dashboard">
                    <dashboard :execution='execution'></dashboard>
                </b-tab>
                <b-tab title="Execution Graph">
                    <graph :execution='execution'></graph>
                </b-tab>
                <b-tab title="Dataset Explorer">
                    <dataset :execution='execution'></dataset>
                </b-tab>
                <b-tab title="Experimenter">
                    <experimenter :execution='execution'></experimenter>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>

<script>
import details from './view/system-details'
import usage from './view/system-usage'
import dashboard from './view/dashboard'
import graph from './view/graph'
import dataset from './view/dataset'
import experimenter from './view/experimenter'

export default {
    name: 'Viewer',
    components: {
        'system-details': details,
        'system-usage': usage,
        'dashboard': dashboard,
        'graph': graph,
        'dataset': dataset,
        'experimenter': experimenter
    },
    watch: {
        '$route': function (to, from) {
            var id = this.$route.params.id

            if (id in this.$store.state.executions) {
                return this.$store.state.executions[id]
            }

            window.notify.showError('Execution', 'Client currently not connected neither available on logs')
            this.$router.push('/')
        }
    },
    computed: {
        execution () {
            return this.$store.getters.currentExecution
        }
    }
}
</script>
