# pylint: disable=I1101 # no-member
# pylint: disable=R0903 # too-few-public-methods

from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
