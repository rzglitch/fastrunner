from flask import render_template, Blueprint

from app.service.board import BoardService

bp = Blueprint('board', __name__)


@bp.route('/<string:name>')
def board_entries(name):
    entries = BoardService.get_entry_list(name, 0)
    return render_template('board/get_entries.html', entries=entries)


@bp.route('/<string:name>/add')
def board_add_entry(name):
    return render_template('board/add_entry.html')


@bp.route('/<string:name>/add', methods=['POST'])
def board_add_entry_post(name):

    return None


@bp.route('/update/<int:id>')
def update_entry(id):
    return render_template('board/update_entry.html')


@bp.route('/update/<int:id>', methods=['POST'])
def update_entry_post(id):

    return None


@bp.route('/delete/<int:id>')
def delete_entry(id):
    return render_template('board/delete_entry.html')


@bp.route('/delete/<int:id>', methods=['POST'])
def delete_entry_post(id):

    return None
