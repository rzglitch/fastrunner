from flask import render_template, Blueprint

from app.service.entry import EntryService

bp = Blueprint('board', __name__)


@bp.route('/read/<int:id>')
def read_entry(id):
    entry = EntryService.get_entry(id)
    return render_template('entry/read_entry.html', entry=entry)


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
