from sqlalchemy import MetaData

from elixir import Entity, has_field, belongs_to, has_many, String


metadata = MetaData()


class Application(Entity):
    has_field('title', String(31))
    has_field('package_name', String(31))
    has_field('egg_name', String(31))
    has_field('dburi', String(127))
    has_field('description', String)

    alternate_ids = ['package_name']

    @property
    def model(self):
        model = getattr(self, '_model', None)
        if model is None:
            imp_args = globals(), locals(), ['']
            base = __import__('%s.lib.base' % self.package_name, *imp_args)
            model = getattr(base, 'model', None)
            if model is None:
                model = __import__('%s.models' % package_name, *imp_args)
            self._model = model
        return model

    def __str__(self):
        return 'Application: %s' % self.title

    def __repr__(self):
        return str(self)
