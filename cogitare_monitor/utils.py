def assert_valid_plugin(plugin):
    required = ['name', 'view', 'cogitare', 'monitor']
    types = [str, (str), dict, dict]

    assert isinstance(plugin, dict)

    for req_name, req_type in zip(required, types):
        assert req_name in plugin
        assert isinstance(plugin[req_name], req_type)
