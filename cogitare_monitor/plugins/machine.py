def on_machine(manager, sid, machine):
    execution = manager.execution_by_sid(sid)
    execution.machine = machine
    manager.monitor.emit('update_machine', {'id': execution.id, 'machine': machine})


PLUG = {
    'name': 'System Details',
    'view': '',
    'cogitare': {
        'machine': on_machine
    },
    'monitor': {
    }
}


__all__ = ['PLUG']
