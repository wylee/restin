from restin.lib.base import *


class DataController(restler.BaseController(model)):
    def __init__(self):
        route = request.environ['routes.route']
        route_info = request.environ['pylons.routes_dict']

        application_id = route_info['application_id']
        app = self._get_entity_or_404(model.Application, application_id)
        self.model = model_registry[app.package_name]

        c_name = route_info['collection_name']
        m_name = request.params.get('m', None)
        if m_name is None:
            if c_name.endswith('s'):
                m_name = c_name[:-1]
            else:
                m_name = c_name

        route.member_name = m_name
        route.collection_name = c_name

        super(DataController, self).__init__()
