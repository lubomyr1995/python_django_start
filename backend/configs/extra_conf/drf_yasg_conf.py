SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': None,
    'DEFAULT_PAGINATOR_INSPECTORS': (
        'core.pagination.pagination_inspector.PaginationInspector',
        'drf_yasg.inspectors.CoreAPICompatInspector'
    )
}