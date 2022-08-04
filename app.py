from flask import Flask, request, render_template, redirect, url_for
from database import User, app, db




@app.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["nm"]
        surname = request.form['surnm']
        phone_num = request.form['phone']
        address = request.form['address']

        if len(name) == 1 or len(surname) == 1:
            raise ValueError("It's not a valid name or surname")
        elif not name.isalpha() or not surname.isalpha():
            raise ValueError("All characters for name and surname should be letters")
        elif len(phone_num) != 9 or not phone_num.isnumeric():
            raise ValueError("Must contain only 9 digits(i.e. 0xxxxxxxx)")
        elif db.session.query(User).filter(User.phone_num == phone_num).first():
            raise ValueError("The phone number is already registered. Please add another phone number.")
        elif len(address) < 5 or address.isalpha() or address.isnumeric():
            raise ValueError("Not a valid address")
        else:
            user = User(name=name,
                        surname=surname,
                        phone_num=phone_num,
                        address=address)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user", usr = name+ " " +surname))
    return render_template("register.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr} you have successfully registered</h1>"


@app.route('/<phone>/edit/', methods = ["POST", "GET"])
def edit(phone):
    user = User.query.get_or_404(phone)
    # user= db.session.query(User).filter(User.phone_num == str(phone))
    if request.method == "POST":
        name = request.form["nm"]
        surname = request.form['surnm']
        phone_num = request.form['phone']
        address = request.form['address']

        if len(name) == 1 or len(surname) == 1:
            raise ValueError("It's not a valid name or surname")
        elif not name.isalpha() or not surname.isalpha():
            raise ValueError("All characters for name and surname should be letters")
        elif len(phone_num) != 9 or not phone_num.isnumeric():
            raise ValueError("Must contain only 9 digits(i.e. 0xxxxxxxx)")
        elif db.session.query(User).filter(User.phone_num == phone_num).first():
            raise ValueError("The phone number is already registered. Please add another phone number.")
        elif len(address) < 5 or address.isalpha() or address.isnumeric():
            raise ValueError("Not a valid address")
        else:
            user.name = name
            user.surname = surname
            user.phone_num = phone_num
            user.address = address

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user_edit", usr_edit=name + " " + surname))
    return render_template("edit.html", user = user)


@app.route("/<usr_edit>/edited")
def user_edit(usr_edit):
    return f"<h1>{usr_edit} you have successfully updated your info</h1>"


@app.route('/<phone>/delete/')
def delete(phone):
    user = User.query.get_or_404(phone)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_delete'))

@app.route("/deleted/")
def user_delete():
    return f"<h1> You have successfully deleted your data </h1>"


if __name__ == "__main__":
    app.run(debug = True)




