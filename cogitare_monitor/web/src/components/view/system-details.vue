<template>
    <b-container fluid class='system-details' v-if='execution != null'>
        <b-row>
            <b-col><h3>{{execution.name}}</h3></b-col>
        </b-row>
        <b-row><b-col><p class="text-muted">{{execution.description}}</p></b-col></b-row>
        <hr>
        <b-row>
            <b-card v-if='execution.machine' title="System Details" class='w-100' sub-title="Basic details of the machine running this Execution. CPU, GPU, RAM, etcs.">
                <br>

                <b-container fluid>
                    <b-row><b-col class='col-2'><b>Platform: </b></b-col><b-col>{{execution.machine.platform}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>OS: </b></b-col><b-col>{{execution.machine.os}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>OS Release: </b></b-col><b-col>{{execution.machine.os_release}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Hostname: </b></b-col><b-col>{{execution.machine.hostname}}</b-col></b-row>
                    <hr>

                    <b-row><b-col class='col-2'><b>Total RAM: </b></b-col><b-col>{{execution.machine.total_ram}} GBs</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Total Swap: </b></b-col><b-col>{{execution.machine.total_swap}} GBs</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Architecture Type: </b></b-col><b-col>{{execution.machine.type}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Count of Logical CPUs: </b></b-col><b-col>{{execution.machine.num_cpu}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Count of Physical CPUs: </b></b-col><b-col>{{execution.machine.num_cpu_real}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Count of Usable CPUs: </b></b-col><b-col>{{execution.machine.usable_cpu}}</b-col></b-row>
                    <b-row v-for='(cpu, index) in execution.machine.min_max_cpus' :key='index'>
                        <b-col class='col-2'><b>CPU {{index + 1}}: </b></b-col><b-col>Min: {{cpu[0]}} Mhz | Max: {{cpu[1]}} Mhz</b-col>
                    </b-row>
                    <hr>
                    <b-row v-if='!execution.machine.nvidia'><b-col class='col-2'><b>GPUs</b></b-col><b-col>Could not get GPU information (if using, check if NVML is installed). </b-col></b-row>
                    <div v-if='execution.machine.nvidia'>
                        <b-row><b-col class='col-2'><b>Nvidia Driver Version</b></b-col><b-col>{{execution.machine.gpu.driver_version}}</b-col></b-row>
                        <div v-for='(gpu, index) for gpu in execution.machine.gpu.devices' :key='index'>
                            <br>
                            <b-row ><b-col class='col-2'><b>GPU {{index + 1}}</b></b-col><b-col>{{gpu.name}}</b-col></b-row>
                            <b-row ><b-col class='col-2'><b>Graphic Clock</b></b-col><b-col>{{gpu.clock}} Mhz | Max {{gpu.clock_max}} Mhz</b-col></b-row>
                            <b-row ><b-col class='col-2'><b>Memory Clock</b></b-col><b-col>{{gpu.clock_mem}} Mhz | Max {{gpu.clock_mem_max}} Mhz</b-col></b-row>
                            <b-row ><b-col class='col-2'><b>Memory</b></b-col><b-col>{{gpu.memory}} GBs</b-col></b-row>
                        </div>
                    </div>
                    <hr>

                    <b-row><b-col class='col-2'><b>Python Version: </b></b-col><b-col>{{execution.machine.python_version}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Process ID: </b></b-col><b-col>{{execution.machine.pid}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Process Created at: </b></b-col><b-col>{{execution.machine.create_time}}</b-col></b-row>
                    <b-row><b-col class='col-2'><b>Environment Variables: </b></b-col><b-col>
                            <b-btn v-b-toggle.environ class="btn-sm" variant='info'>View/Hide System Variables</b-btn>

                            <b-collapse id="environ">
                                <b-container fluid>
                                    <div v-for='(value, name) in execution.machine.environ'>
                                        <b-row>
                                            <b-col class='col-2'><b>{{name}}: </b></b-col><b-col>{{value}}</b-col>
                                        </b-row>
                                    </div>
                                </b-container>
                            </b-collapse>
                    </b-col></b-row>

                </b-container>
            </b-card>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'system-details',
    props: ['execution']
}
</script>
