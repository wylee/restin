from pylons import Response, c, g, cache, request, session
from pylons.controllers import WSGIController
from pylons.decorators import jsonify, validate
from pylons.templating import render, render_response
from pylons.helpers import abort, redirect_to, etag_cache
from pylons.i18n import N_, _, ungettext
from pylons.database import create_engine

import restin.models as model
import restin.lib.helpers as h

import restler


RestController = restler.BaseController(model)


model_registry = {'restin': model}

def register_model(app):
    package_name = app.package_name
    engine = create_engine(uri=app.dburi, echo=0)
    restler.init_model(app.model)
    app.model.metadata.connect(engine)
    model_registry[package_name] = app.model

def register_models():
    apps = model.Application.select()
    for app in apps:
        register_model(app)

register_models()


class BaseController(WSGIController): pass


__all__ = [__n for __n in locals().keys() if not __n.startswith('_')]
__all__.append('_')
