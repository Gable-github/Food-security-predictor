import os
from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import CreateQuestionForm
from app.models import Dataset_climate
from app.serverlibrary import malnourished
# from werkzeug.urls import url_parse
from app import db
from flask import request 

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html', title='Home')

@application.route('/climate', methods = ["GET", "POST"])
def climate():
	form = CreateQuestionForm()
	# if os.path.exists('static/myplot.png'):
	# 	pass
	# else:
	# 	malnourished()
	malnourished()
	if form.validate_on_submit():
		answer = Dataset_climate.query.filter_by(indep_var=form.indep_var.data).first()
		# flash('Here is the predicted price for the specified indep var.')
		return render_template('climate.html', title='Climate', form=form)
		# return render_template('climate.html', title='Climate', question=form.indep_var.data, answer=answer, form=form)
	return render_template('climate.html', title='Climate', form=form, image_path='myplot.png')

if __name__ == '__main__':
    app.run(debug=True)

# @application.route('/challenges', methods=['GET', 'POST'])
# @login_required
# def challenges():
# 	challenges = current_user.challenges.all()
# 	form = ChallengeAnswerForm()
# 	recordsquery = TimeRecord.query.filter_by(user_id=current_user.id).all()
# 	records = { c.id: r.elapsed_time for r in recordsquery for c in challenges if r.challenge_id== c.id}
# 	if form.validate_on_submit():
# 		record = TimeRecord()
# 		record.elapsed_time = int(form.elapsed_time.data)
# 		record.challenge_id = int(form.challenge_id.data)
# 		record.user_id = current_user.id
# 		answer = form.answer.data
# 		challenge = Challenge.query.filter_by(id=form.challenge_id.data).first()
# 		if int(answer) == int(challenge.question.answer):
# 			db.session.add(record)
# 			db.session.commit()
# 			challenges = current_user.challenges.all()
# 			recordsquery = TimeRecord.query.filter_by(user_id=current_user.id).all()
# 			records = { c.id: r.elapsed_time for r in recordsquery for c in challenges if r.challenge_id== c.id}
# 			form.answer.data = ""
# 			return render_template('challenges.html', title='Challenges',
# 							user=current_user,
# 							challenges=challenges,
# 							form = form,
# 							records = records)
		
# 		return redirect(url_for('challenges'))
# 	form.answer.data=""
# 	return render_template('challenges.html', title='Challenges',
# 							user=current_user,
# 							challenges=challenges,
# 							form = form,
# 							records = records)

# @application.route('/halloffame')
# def halloffame():
# 	challenges = Challenge.query.all()
# 	records = { c.id:get_smallest_three(c) for c in challenges}
# 	print(records)
# 	return render_template('halloffame.html', title="Hall of Fame",
# 							challenges=challenges,
# 							records=records)

# @application.route('/login', methods=['GET', 'POST'])
# def login():
# 	if current_user.is_authenticated:
# 		return redirect(url_for('index'))

# 	form = LoginForm()

# 	if form.validate_on_submit():
# 		user = User.query.filter_by(username=form.username.data).first()
# 		if user is None or not user.check_password(form.password.data):
# 			flash('Invalid username or password')
# 			return redirect(url_for('login'))
# 		login_user(user, remember=form.remember_me.data)
# 		next_page = request.args.get('next')
# 		if not next_page or url_parse(next_page).netloc != '':
# 			next_page = url_for('index')
# 		return redirect(next_page)
# 	return render_template('login.html', title='Sign In', form=form)

# @application.route('/logout')
# def logout():
# 	logout_user()
# 	return redirect(url_for('index'))

# @application.route('/register', methods=['GET', 'POST'])
# def register():
# 	if current_user.is_authenticated:
# 		return redirect(url_for('index'))
# 	form = RegistrationForm()
# 	if form.validate_on_submit():
# 		user = User(username=form.username.data)
# 		user.set_password(form.password.data)
# 		db.session.add(user)
# 		db.session.commit()
# 		flash('Congratulations, you are now a registered user.')
# 		return redirect(url_for('login'))
# 	return render_template('register.html', title='Register', form=form)