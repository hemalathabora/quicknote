from flask import Flask, render_template, request, redirect, url_for, abort
from models import db, Note
from flask import send_file
import io
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    query = request.args.get('search')
    tag_filter = request.args.get('tag')

    notes_query = Note.query

    if query:
        notes_query = notes_query.filter(
            (Note.title.contains(query)) |
            (Note.content.contains(query)) |
            (Note.tags.contains(query))
        )

    if tag_filter:
        notes_query = notes_query.filter(Note.tags.contains(tag_filter))

    notes = notes_query.order_by(Note.is_pinned.desc(), Note.id.desc()).all()

    # Get all unique tags from all notes
    all_tags = set()
    for note in Note.query.all():
        if note.tags:
            for t in note.tags.split(','):
                all_tags.add(t.strip())

    return render_template('index.html', notes=notes, search_query=query, all_tags=sorted(all_tags), current_tag=tag_filter)

@app.route ('/view/<int:note_id>')
def view_note(note_id):
    note = Note.query.get_or_404 (note_id)
    return render_template ('view_note.html', note=note)


@app.route ('/export/<int:note_id>')
def export_note(note_id):
    note = Note.query.get_or_404 (note_id)
    content = f"Title: {note.title}\n\nTags: {note.tags}\n\n{note.content}"

    buffer = io.BytesIO ()
    buffer.write (content.encode ('utf-8'))
    buffer.seek (0)

    filename = f"{note.title.replace (' ', '_')}.txt"
    return send_file (buffer, as_attachment=True, download_name=filename, mimetype='text/plain')


@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        new_note = Note(title=title, content=content, tags=tags)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/pin/<int:note_id>', methods=['POST'])
def pin_note(note_id):
    note = Note.query.get_or_404(note_id)
    note.is_pinned = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/unpin/<int:note_id>', methods=['POST'])
def unpin_note(note_id):
    note = Note.query.get_or_404(note_id)
    note.is_pinned = False
    db.session.commit()
    return redirect(url_for('index'))
@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        note.tags = request.form['tags']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_note.html', note=note)
@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
