from app import db,bcrypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String(255))

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self, password):
        return bcrypt.check_password_hash(password)

    @classmethod
    def get_username(cls, username):
        return cls.query.filter_by(username=username).first()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return f"Post('{self.title}', '{self.publication_date}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    parent_comment = db.relationship('Comment', remote_side=[id])

    def __repr__(self):
        return f"Comment('{self.text}', '{self.publication_date}')"


class Reaction(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    reaction_type = db.Column(db.String(10), nullable=False)  # 'like' or 'dislike'
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('reactions', lazy=True))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reactions', lazy=True))

    def __repr__(self):
        return f"Reaction('{self.reaction_type}')"


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Tag('{self.name}')"


class Subscription(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)

    def __repr__(self):
        return f"Subscription('{self.email}')"


class Analytics(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('analytics', lazy=True))
    page_views = db.Column(db.Integer(), default=0)
    unique_visitors = db.Column(db.Integer(), default=0)



