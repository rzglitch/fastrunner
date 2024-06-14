from flask import render_template, Blueprint, jsonify

from app.service.EntryService import EntryService
from app.form.EntryForm import AddEntryForm, UpdateEntryForm

bp = Blueprint('entry', __name__)


@bp.route('/add', methods=['POST', 'PUT'])
def add_entry_post():
    form = AddEntryForm()
    add_entry = EntryService.add_entry(form)

    if 'error' in add_entry and add_entry['error']:
        return jsonify(add_entry), 400
    else:
        return jsonify(add_entry), 200


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


@bp.route('/update/<string:uuid>', methods=['POST', 'PATCH'])
def entry_update_post(uuid):
    form = UpdateEntryForm()
    update_entry = EntryService.update_entry(uuid, form)

    if 'error' in update_entry and update_entry['error']:
        return jsonify(update_entry), 400
    else:
        return jsonify(update_entry), 200


@bp.route('/delete/<string:uuid>', methods=['POST', 'DELETE'])
def entry_delete_post(uuid):
    delete_entry = EntryService.delete_entry(uuid)

    if 'error' in delete_entry and delete_entry['error']:
        return jsonify(delete_entry), 400
    else:
        return jsonify(delete_entry), 200
