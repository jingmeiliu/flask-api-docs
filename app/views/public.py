from flask import Blueprint

from app.utils.views import resp_by_status

public_bp = Blueprint('public', __name__)


# 公共模块
@public_bp.route('/welcome')
def get_welcome():
    """
        target===/public/welcome;
        description===获取欢迎页面接口;
        method===GET;
        parameter===
            参数名:参数描述,约束
        ;
        response==={
            code:200
            data:[]
            msg:欢迎来到/public/welcome
        }
        """
    msg = '欢迎来到/public/welcome'

    return resp_by_status(0, msg)
