from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa.core import utils
from rasa.core.agent import Agent, Domain
from rasa.utils.io import configure_colored_logging

if __name__ == "__main__":
    configure_colored_logging(loglevel="DEBUG")

    agent = Agent(
        domain=Domain.load("../domain.yml")
    )
    agent.tr