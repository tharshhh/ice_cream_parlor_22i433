from flask import Flask, render_template, request, redirect, url_for
from . import db
from .models import Flavor, Allergen
from .forms import FlavorForm, AllergenForm

# Create the app instance
app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    form = FlavorForm()
    if form.validate_on_submit():
        new_flavor = Flavor(name=form.name.data, description=form.description.data)
        db.session.add(new_flavor)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_flavor.html', form=form)

@app.route('/allergens', methods=['GET', 'POST'])
def allergens():
    form = AllergenForm()
    if form.validate_on_submit():
        new_allergen = Allergen(name=form.name.data)
        db.session.add(new_allergen)
        db.session.commit()
        return redirect(url_for('allergens'))
    allergens = Allergen.query.all()
    return render_template('allergens.html', form=form, allergens=allergens)

if __name__ == "__main__":
    app.run(debug=True)
