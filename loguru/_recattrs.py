class LevelRecattr:
    __slots__ = ("name", "no", "icon")

    def __init__(self, name, no, icon):
        self.name = name
        self.no = no
        self.icon = icon

    def __format__(self, spec):
        return self.name.__format__(spec)


class FileRecattr:
    __slots__ = ("name", "path")

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __format__(self, spec):
        return self.name.__format__(spec)


class ThreadRecattr:
    __slots__ = ("id", "name")

    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def __format__(self, spec):
        return self.id.__format__(spec)


class ProcessRecattr:
    __slots__ = ("id", "name")

    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def __format__(self, spec):
        return self.id.__format__(spec)


class ExceptionRecattr:
    __slots__ = ("type", "value", "traceback")

    def __init__(self, type_, value, traceback):
        self.type = type_
        self.value = value
        self.traceback = traceback

    def __getitem__(self, index):
        return (self.type, self.value, self.traceback)[index]

    def __reduce__(self):
        exception = (self.type, self.value, None)  # tracebacks are not pickable
        return (ExceptionRecattr, exception)
