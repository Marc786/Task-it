class ServiceLocator(object):
    __dependencies = {}

    @classmethod
    def register_dependency(cls, dependency_class, service, replace_allowed=False):
        if dependency_class in cls.__dependencies and not replace_allowed:
            raise Exception(
                f"Dependency {dependency_class.__name__} already registered"
            )
        cls.__dependencies[dependency_class] = service

    @classmethod
    def get_dependency(cls, dependency_class):
        if dependency_class not in cls.__dependencies:
            raise Exception(f"Dependency {dependency_class.__name__} not registered")
        return cls.__dependencies[dependency_class]

    @classmethod
    def clear(cls):
        cls.__dependencies.clear()
