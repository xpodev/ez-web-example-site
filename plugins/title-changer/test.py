import ez
import ez.plugins
from ez_plugins import test_plugin


def run():
    # my_api returns if x is greater than y
    if test_plugin.my_api(2, 1):
        text = [f"Loaded {len(ez.plugins.get_plugins())} plugins:"]
        for plugin in ez.plugins.get_plugins():
            text.append(' '.join(('\t\t', plugin.info.name, f"v{plugin.info.version}")))
        ez.log.info('\n'.join(text))
