<template>
    <b-container fluid class='system-usage' v-if='execution != null'>
        <b-row>
            <b-col><h3>{{execution.name}}</h3></b-col>
            <b-col>
                <b-button v-if='execution.connected == true' v-on:click='watch' class='float-right' variant="info">Enable/Disable System Usage Monitor</b-button>
            </b-col>
        </b-row>
        <b-row><b-col><p class="text-muted">{{execution.description}}</p></b-col></b-row>
        <hr>
        <b-row>
            <b-card title="System Usage" class='w-100' sub-title="Display real-time plots of the resource usage. The resource usage tracking runs in a separated thread to avoid
                performance impact.">
                <br>

                <b-container fluid v-if='execution._plots'>
                    <b-row v-for='plot in execution._plots' :key='plot.name' :id='"usage_" + plot.name' class='plot-holder'>
                    </b-row>
                    <br><br>
                </b-container>
            </b-card>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'system-usage',
    props: ['execution'],
    computed: {
        plots () {
            return this.execution._plots
        }
    },
    created: function () {
        this.plotted = []
    },

    mounted: function () {
        this.update_plots(this.plots)
    },
    methods: {
        watch: function (event) {
            Object.keys(this.execution._plots).forEach(function (prop) {
                delete this.execution._plots[prop]
            })
            this.$socket.emit('toggle_system_usage', this.execution.id)
        },

        update_plots: function (plots) {
            let self = this
            setTimeout(function () {
                for (var plot in plots) {
                    if (self.plotted.indexOf(plot) > -1) {
                        continue
                    }
                    self.plotted.push(plot)

                    let root = document.getElementById('usage_' + plot)
                    let s = document.createElement('script')
                    s.id = plots[plot].plot_id
                    s.src = plots[plot].plot_src
                    s.setAttribute('data-bokeh-model-id', plots[plot].plot_model_id)
                    s.setAttribute('data-bokeh-doc-id', '')
                    root.appendChild(s)
                }
            }, 1000)
        }
    },
    watch: {
        plots (newValue, old) {
            this.update_plots(newValue)
        }
    }
}
</script>

<style>
.plot-holder {
    height: 300px;
    padding: 10px;
}
</style>
