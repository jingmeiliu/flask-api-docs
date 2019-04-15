from flask import jsonify, abort

status_mapping = {
    # location
    1012: '该区域下存在已绑定的城市',
    1022: '该城市下存在已绑定的数据中心',
    1032: '该数据中心下存在已绑定的节点',

    # common
    4000: '参数错误',
    4001: '记录不存在',
    4002: '记录已存在',

    5000: '其他未知错误'
}


def resp_with_data(data=None):
    if data is None:
        return jsonify({'status': 0})

    return jsonify({'status': 0, 'data': data})


def resp_by_status(status, message=None):
    """
    根据自定义错误status生成响应数据
    """
    if message is None:
        message = status_mapping.get(status, None)
    return jsonify({'status': status, 'message': message})


# 缺少参数判断
def gen_400(*args):
    # 400错误还应包含接收到空值以外的情况，暂时跳过
    if None in args:
        abort(400)


# 获取数据为空判断
def gen_404(queryset):
    if not queryset:
        abort(404)
