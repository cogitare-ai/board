<template>
    <div class="Config">
        <b-card>
            <b-container fluid>
                <b-row>
                    <b-col><h3>Configuration</h3></b-col>
                </b-row>
                <b-row><b-col><p class="text-muted">Cogitare's Monitor settings</p></b-col></b-row>
                <hr>
                <b-alert show variant="warning">Feature scheduled for a future release.</b-alert>
                You can contribute with ideias, with code, or track the development of this feature at
                <a href="https://github.com/cogitare-ai/monitor/issues/5">https://github.com/cogitare-ai/monitor/issues/5</a>
            </b-container>
        </b-card>
    </div>
</template>

<script>
export default {
    name: 'Config',
    data () {
        return {
            msg: 'Config page'
        }
    }
}
</script>
