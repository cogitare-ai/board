<template>
    <b-container fluid class='graph' v-if='execution != null'>
        <b-row>
            <b-col><h3>{{execution.name}}</h3></b-col>
        </b-row>
        <b-row><b-col><p class="text-muted">{{execution.description}}</p></b-col></b-row>
        <hr>
        <b-row>
            <b-card v-if='execution.machine' title="DataSet Explorer" class='w-100' sub-title="Explore and analyze the model dataset. You can debug the data loading time, buffer usage, grab samples, and more.">
                <br>

                <b-alert show variant="warning">Feature scheduled for a future release.</b-alert>
                You can contribute with ideias, with code, or track the development of this feature at
                <a href="https://github.com/cogitare-ai/monitor/issues/3">https://github.com/cogitare-ai/monitor/issues/3</a>
            </b-card>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'dataset',
    props: ['execution']
}
</script>
