from restin.lib.base import *


class DataController(restler.BaseController(model)):
    def __init__(self):
        route = request.environ['routes.route']
        route_info = request.environ['pylons.routes_dict']

        application_id = route_info['application_id']
        app = self._get_entity_or_404(model.Application, application_id)
        self.model = model_registry[app.package_name]

        entity_name = route_info['entity_name']
        collection_name = '%ss' % entity_name

        route.member_name = entity_name
        route.collection_name = collection_name

        super(DataController, self).__init__()
