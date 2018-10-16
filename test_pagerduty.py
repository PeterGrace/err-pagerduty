pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'

def test_pagerduty(testbot):
    testbot.push_message('!oncall')
    assert 'Yisss' in testbot.pop_message()
