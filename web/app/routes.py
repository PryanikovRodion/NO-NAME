
from flask import render_template, flash, redirect, url_for, request
from app import app,db, store, Buyer, Saler, Product
from app.forms import LoginForm, RegistrationForm, SalerAddProductForm, BuyerAddMoneyForm, BuyProductForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from urllib.parse import urlparse



@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data,role=form.role.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        if user.role == "buyer":
            buyer = Buyer(user.username,user.email)
            store.add_user(buyer)
        elif user.role == "saler":
            saler = Saler(user.username)
            store.add_user(saler)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = BuyerAddMoneyForm()
    if form.validate_on_submit():
        store.buyers[current_user.username].money += form.money.data
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('profile')
        return redirect(next_page)
    return render_template("profile.html",title="Profile", store=store, form=form)

@app.route('/saler_add_product',methods=['GET', 'POST'])
@login_required
def saler_add_product():
    if current_user.role != "saler":
        return redirect(url_for('profile'))
    form = SalerAddProductForm()
    if form.validate_on_submit():
        store.salers[current_user.username].products[form.name.data] = Product(form.name.data,form.price.data,form.count.data)
        store.salers[current_user.username].update_products()
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('profile')
        return redirect(next_page)
    return render_template('addproduct.html', title='Add product', form=form)

@app.route('/catalog',methods=['GET', 'POST'])
def catalog():
    form=BuyProductForm()
    if form.validate_on_submit():
        try:
            store.transaction(form.salername.data,form.productname.data,current_user.username,form.count.data)
        except Exception as er:
            flash(er)
    return render_template('catalog.html', title='Catalog',store=store, form=form)
    
@app.route('/orders')
@login_required
def orders():
    return render_template("orders.html", title='Orders', store=store)