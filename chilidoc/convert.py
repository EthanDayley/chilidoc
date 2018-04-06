"""
This module provides functions and classes to convert
ChiliDoc to html, etc.
"""

class HtmlConverter:
    # the prefix attached to generated classes
    _class_prefix: str

    # the asciidoc string to convert
    _asciidoc: str

    @property
    def class_prefix(self) -> str:
        return self._class_prefix

    @class_prefix.setter
    def class_prefix(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string for "
                            "class_prefix, got \"%s\"" % type(value))
        else:
            self._class_prefix = value

    @property
    def asciidoc(self) -> str:
        return self._asciidoc

    @asciidoc.setter
    def asciidoc(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError("Expected string for "
                            "asciidoc, got \"%s\"" % type(value))
        else:
            self._asciidoc = value

    def __init__(self, *args, **kwargs):
        """
        Class to convert chilidoc to html
        """
        if len(args) == 1:
            self.asciidoc = args[0]
        elif len(args) > 1:
            raise TypeError("Expected at most 1 arguments,"
                            "got %d" % len(args))
        for name in kwargs:
            if name == "asciidoc":
                self.asciidoc = kwargs[name]
            elif name == "class_prefix":
                self.class_prefix = kwargs[name]
            else:
                raise TypeError("Got an unexpected argument '%s'"
                                % name)
