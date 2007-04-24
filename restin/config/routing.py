"""
Setup your Routes options here
"""
import os
from routes import Mapper


def make_map(global_conf={}, app_conf={}):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    map = Mapper(directory=os.path.join(root_path, 'controllers'))
    map.connect('error/:action/:id', controller='error')

    map.resource('application', 'applications')

    GET_condition = dict(method=['GET'])
    POST_condition = dict(method=['POST'])
    PUT_condition = dict(method=['PUT'])
    DELETE_condition = dict(method=['DELETE'])

    route = 'applications/:application_id/:controller/:collection_name'
    
    kw = dict(action='create', conditions=POST_condition)
    map.connect(route, **kw)
    
    kw = dict(action='index', conditions=GET_condition)
    map.connect(route, **kw)
    map.connect(route + '.:(format)', **kw)
    
    kw = dict(action='new', conditions=GET_condition)
    map.connect(route + '/new', **kw)
    map.connect(route + '/new.:(format)', **kw)
    
    kw = dict(action='update', conditions=PUT_condition)
    map.connect(route + '/:id', **kw)
    
    kw = dict(action='delete', conditions=DELETE_condition)
    map.connect(route + '/:id', **kw)
    
    kw = dict(action='edit', conditions=GET_condition)
    map.connect(route + '/:(id);edit', **kw)
    map.connect(route + '/:(id).:(format);edit', **kw)

    kw = dict(action='show', conditions=GET_condition)
    map.connect(route + '/:id', **kw)
    map.connect(route + '/:(id).:(format)', **kw)

    map.connect('*url', controller='template', action='view')
    return map
