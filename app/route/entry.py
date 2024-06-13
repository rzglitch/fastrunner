from flask import render_template, redirect, Blueprint

from app.service.EntryService import EntryService
from app.form.EntryForm import AddEntryForm, UpdateEntryForm

bp = Blueprint('entry', __name__)


@bp.route('/add', methods=['POST'])
def add_entry_post():
    form = AddEntryForm()
    add_entry = EntryService.add_entry(form)
    if add_entry:
        return redirect('/board/' + form.data.get('board_name'))


@bp.route('/<string:uuid>')
def entry_read(uuid):
    entry = EntryService.get_entry(uuid)
    return render_template('entry/get_entry.html', data=entry)


@bp.route('/update/<string:uuid>')
def entry_update(uuid):
    form = AddEntryForm()
    entry = EntryService.get_entry(uuid)

    if 'entry' in entry:
        form.content.data = entry['entry']['content']
        form.entry_metadata.data = entry['entry']['entry_metadata']
    return render_template('entry/update_entry.html', data=entry, form=form)


@bp.route('/update/<string:uuid>', methods=['POST'])
def entry_update_post(uuid):
    form = UpdateEntryForm()
    update_entry = EntryService.update_entry(uuid, form)
    if update_entry:
        return str(update_entry)


@bp.route('/delete/<string:uuid>')
def entry_delete_post(uuid):
    delete_entry = EntryService.delete_entry(uuid)
    if delete_entry:
        return str(delete_entry)
