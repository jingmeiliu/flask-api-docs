
from flask import Blueprint
from app.utils.views import resp_with_data

user_bp = Blueprint('user', __name__)


@user_bp.route('/add_user', methods=['POST'])
def add_user():
    """
        target===/user/add_user;
        description===新增用户;
        method===POST;
        parameter===
            name:用户名,required
            desc:描述
        ;
        response==={
            code:201 非201为不成功，信息在msg中
            msg:Created
        }
    """

    return resp_with_data()


