from dataclasses import dataclass

from midimiddleware.components.configuration import Configuration
from midimiddleware.components.port_selector import PortSelector
from midimiddleware.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class Components(metaclass=SingletonMetaclass):
    configuration = Configuration()
    engine = None
    port_selector = PortSelector()
    project_persistence = None
