import ez
import ez.plugins


def run():
    # We put this here because we can't know if the test_plugin is already loaded
    from ez_plugins import test_plugin
    # my_api returns if x is greater than y
    if test_plugin.my_api(2, 1):
        text = [f"Loaded {len(ez.plugins.get_plugins())} plugins:"]
        for plugin in ez.plugins.get_plugins():
            text.append(' '.join(('\t\t', plugin.info.name, f"v{plugin.info.version}")))
        ez.log.info('\n'.join(text))
    
