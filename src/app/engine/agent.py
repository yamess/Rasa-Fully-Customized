from rasa.core.agent import Agent
from typing import Union, List, Optional, Text

from rasa.core.http_interpreter import RasaNLUHttpInterpreter
from rasa.core.lock_store import LockStore
from rasa.core.nlg import NaturalLanguageGenerator
from rasa.core.tracker_store import TrackerStore
from rasa.shared.core.domain import Domain
from rasa.utils.endpoints import EndpointConfig


class MyAgent(Agent):
    def __init__(
        self,
        domain: Optional[Domain] = None,
        generator: Union[EndpointConfig, NaturalLanguageGenerator, None] = None,
        tracker_store: Optional[TrackerStore] = None,
        lock_store: Optional[LockStore] = None,
        action_endpoint: Optional[EndpointConfig] = None,
        fingerprint: Optional[Text] = None,
        model_server: Optional[EndpointConfig] = None,
        remote_storage: Optional[Text] = None,
        http_interpreter: Optional[RasaNLUHttpInterpreter] = None,
    ):
        super(MyAgent, self).__init__(
            domain,
            generator,
            tracker_store,
            lock_store,
            action_endpoint,
            fingerprint,
            model_server,
            remote_storage,
            http_interpreter,
        )
