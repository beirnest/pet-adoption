from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()

@app.route("/")
def load_home():
    pets = Pet.query.all()
    return render_template("base.html", pets = pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name = name, species = species, image_url = photo_url, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/add")

    else:
        return render_template(
            "pet_add_form.html", form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit Pet Details"""
    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
       
        image_url = form.image_url.data
        notes = form.notes.data
        available = form.available.data
    
        pet.image_url = image_url
        pet.notes = notes
        pet.available = available
        db.session.commit()
        return redirect(f"/{pet_id}")

    else:
        return render_template(
            "edit_pet.html", form=form, pet=pet)


