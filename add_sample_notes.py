from app import app, db
from models import Note

with app.app_context():
    # Clear existing notes if needed
    Note.query.delete()

    # Sample notes
    samples = [
        Note(title="Meeting Notes", content="Discuss project roadmap and deadlines.", tags="work,meeting", is_pinned=True),
        Note(title="Grocery List", content="Milk, Eggs, Bread, Butter", tags="personal,shopping"),
        Note(title="Python Tips", content="Use list comprehensions for cleaner code.", tags="coding,python"),
        Note(title="Book Ideas", content="Sci-fi novel set on Mars.", tags="writing,ideas", is_pinned=True),
        Note(title="Travel Plans", content="Visit Japan in spring.", tags="personal,travel")
    ]

    for note in samples:
        db.session.add(note)

    db.session.commit()
    print("Sample notes added!")
