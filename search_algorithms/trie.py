class Trie:
    """A case-sensitive prefix tree for strings."""

    def __init__(self) -> None:
        self._root: dict[str, dict] = {}
        self._terminal = ""

    def insert(self, word: str) -> None:
        node = self._root
        for character in word:
            node = node.setdefault(character, {})
        node[self._terminal] = {}

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and self._terminal in node

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, text: str) -> dict | None:
        node = self._root
        for character in text:
            if character not in node:
                return None
            node = node[character]
        return node
