"""Abstract base plugin"""

import abc
import typing as t


class DeckPlugin(abc.ABC):
    """Abstract base PyDeck plugin class

    All PyDeck plugins should inherit from this class

    Attributes:
        name: Name of the plugin
        description: Description of the plugin
        author: Author of the plugin

        plugin_id: Unique identifier for variable & action access
            (fallback to file/package name if not set)

        plugin_prefix: String plugin prefix used for variables and actions

        actions: Dictionary of actions (Callables)
        variables: Dictionary of variables

        config: Custom settings editable by user and used by plugin
    """

    name: str
    description: str
    author: str

    plugin_id: str

    actions: dict[str, t.Callable[..., t.Any]]
    variables: dict[str, t.Any]

    config: dict[str, t.Any]

    # @abc.abstractmethod
    def __init__(self) -> None:
        self.actions = {}
        self.variables = {}
        self.config = {}

    @abc.abstractmethod
    def load(self) -> None:
        """Plugin's load"""

    @abc.abstractmethod
    def update(self) -> None:
        """Plugin's update"""
