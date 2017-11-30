<template>
    <b-container fluid class='dashboard' v-if='execution != null'>
        <b-row>
            <b-col><h3>{{execution.name}}</h3></b-col>
        </b-row>
        <b-row><b-col><p class="text-muted">{{execution.description}}</p></b-col></b-row>
        <hr>
        <b-row>
            <b-card v-if='execution.machine' title="Training Dashboard" class='w-100' sub-title="Analyse the training in real time by plots of the model loss, custom model metrics, weight distributions, and more.">
                <br>

                <b-alert show variant="warning">Feature scheduled for a future release.</b-alert>
                You can contribute with ideias, with code, or track the development of this feature at
                <a href="https://github.com/cogitare-ai/monitor/issues/1">https://github.com/cogitare-ai/monitor/issues/1</a>
            </b-card>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'dashboard',
    props: ['execution']
}
</script>
