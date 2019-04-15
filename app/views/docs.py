from flask import Blueprint, url_for, render_template, current_app

docs_bp = Blueprint('docs', __name__)
# (docs路径,接口描述,api路径)
api_list = [
    {
        'name': '公共类接口',
        'list': [
            ('get_menu', '来到public/get_menu', 'public/get_menu'),
        ]
    },
    {
        'name': 'user模块',
        'list': [
            ('add_user', '新增用户', 'user/add_user'),

        ]
    },

]


@docs_bp.route('/')
def index():
    """Redirect home page to docs_bp page."""

    docs_url = url_for('docs.index', _external=True)
    return render_template('api_index.html', api_maps=api_list, docs_url=docs_url)


@docs_bp.route('/<endpoint>')
def show(endpoint):
    """Document page for an endpoint."""
    api = {
        'endpoint': endpoint,
        'doc': '',
    }
    try:
        func = current_app.view_functions[endpoint]
        api = _get_api(func)
    except:
        api['doc'] = 'Invalid logic endpoint: "{}"!'.format(endpoint)
    return render_template('api_docs.html', api=api)


def _get_api_name(func):
    """e.g. Convert 'do_work' to 'Do Work'"""
    words = func.__name__.split('_')
    words = [w.capitalize() for w in words]
    return ' '.join(words)


def _get_api_doc(func):
    if func.__doc__:
        return func.__doc__
    else:
        return 'No doc found for this API!'


def _get_api(func):
    api_docs = {}
    items = _get_api_doc(func).split(';')
    for item in items:
        if item:
            item = item.strip()
            if item:
                item = item.split("===")
                api_docs[item[0]] = item[1]

    return api_docs
