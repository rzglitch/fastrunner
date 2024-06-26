from flask import render_template, Blueprint, jsonify

from app.service.BoardService import BoardService
from app.form.BoardForm import CreateBoardForm
from app.form.EntryForm import AddEntryForm

bp = Blueprint('board', __name__)


@bp.route('/create')
def board_create():
    form = CreateBoardForm()
    return render_template('board/create_board.html', form=form)


@bp.route('/create', methods=['POST', 'PUT'])
def board_create_put():
    form = CreateBoardForm()
    add_board = BoardService.add_board(form)

    if 'error' in add_board and add_board['error']:
        return jsonify(add_board), 400
    else:
        return jsonify(add_board), 200


@bp.route('/<string:name>')
def board_entries(name):
    entries = BoardService.get_entry_list(name, 0)
    return render_template('board/get_entries.html', entries=entries)


@bp.route('/<string:name>/add')
def board_add_entry(name):
    form = AddEntryForm()
    return render_template('board/add_entry.html',
                           form=form, name=name)
