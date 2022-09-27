from pill_my_heart import db

# 유저 정보
class User(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(30))
    re_dt = db.Column(db.String(500))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 병 정보
class Medical_Info(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    medical_cd = db.Column(db.String(25))
    medical_nm = db.Column(db.String(255))
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))

#병력 정보
class Medical_History(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    user_seq =db.Column(db.Integer, primary_key=True)
    medical_cd = db.Column(db.String(25))
    medical_nm = db.Column(db.String(255))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))

# 약 정보
class Medicine_Info(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    medicine_cd = db.Column(db.String(25))
    medicine_nm = db.Column(db.String(255))
    shape_seq = db.Column(db.Integer)
    color_seq = db.Column(db.Integer)
    division_seq = db.Column(db.Integer)
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))
    entp_cd = db.Column(db.String(50))
    entp_nm = db.Column(db.String(255))

# 복용약정보
class Medicine_History(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    user_seq =db.Column(db.Integer, primary_key=True)
    medicine_cd = db.Column(db.String(25))
    medicine_nm = db.Column(db.String(255))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))

# 약 모양
class Medicine_Shape(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    shape = db.Column(db.String(25))
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))

# 약 색상
class Medicine_Color(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(25))
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))

# 약 분할선
class Medicine_Division(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String(25))
    re_dt = db.Column(db.String(500))
    md_dt = db.Column(db.String(500))




