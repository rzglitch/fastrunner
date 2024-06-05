from flask import render_template, redirect, Blueprint

from app.service.entry import EntryService
from app.form.entry import AddEntryForm

bp = Blueprint('entry', __name__)


@bp.route('/add', methods=['POST'])
def add_entry_post():
    form = AddEntryForm()
    add_entry = EntryService.add_entry(form)
    if add_entry:
        return redirect('/board/' + form.data.get('board_name'))


@bp.route('/read/<int:id>')
def entry_read(id):
    entry = EntryService.get_entry(id)
    return render_template('entry/read_entry.html', entry=entry)


@bp.route('/update/<int:id>')
def entry_update(id):
    return render_template('board/update_entry.html')


@bp.route('/update/<int:id>', methods=['POST'])
def entry_update_post(id):

    return None


@bp.route('/delete/<int:id>')
def entry_delete(id):
    return render_template('board/delete_entry.html')


@bp.route('/delete/<int:id>', methods=['POST'])
def entry_delete_post(id):

    return None
