from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix = '/question')

@bp.route('/list/')
def _list():
    q_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/q_list.html', q_list=q_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/q_detail.html', question = question)
