from .extensions import db

class Story(db.Model):
    __tablename__ = 'story'
    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    author_id = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    status = db.Column(db.String(100))
    approved_by_admin_id = db.Column(db.String(255))
    genre = db.Column(db.String(255))  
    category = db.Column(db.String(100))  
    views_count = db.Column(db.Integer, default=0)
    likes_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Story {self.title}>'
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.username}>'
    
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.String(255), primary_key=True)
    story_id = db.Column(db.String(255), db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    story = db.relationship('Story', backref=db.backref('comments', lazy=True))
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    def __repr__(self):
        return f'<Comment {self.id} on Story {self.story_id} by User {self.user_id}>'
    
class Like(db.Model):
    __tablename__ = 'like'
    id = db.Column(db.String(255), primary_key=True)
    story_id = db.Column(db.String(255), db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    story = db.relationship('Story', backref=db.backref('likes', lazy=True))
    user = db.relationship('User', backref=db.backref('likes', lazy=True))

    def __repr__(self):
        return f'<Like {self.id} on Story {self.story_id} by User {self.user_id}>'
    
class AdminActionLog(db.Model):
    __tablename__ = 'admin_action_log'
    id = db.Column(db.String(255), primary_key=True)
    admin_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    target_user_id = db.Column(db.String(255))
    target_story_id = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    admin = db.relationship('User', backref=db.backref('admin_actions', lazy=True))

    def __repr__(self):
        return f'<AdminActionLog {self.action} by Admin {self.admin_id}>'
    
class PasswordResetToken(db.Model):
    __tablename__ = 'password_reset_token'
    id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    expires_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref=db.backref('password_reset_tokens', lazy=True))

    def __repr__(self):
        return f'<PasswordResetToken for User {self.user_id}>'
    
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Genre {self.name}>'
    
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'
    
class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.String(255), primary_key=True)
    reporter_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)
    reported_user_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    reported_story_id = db.Column(db.String(255), db.ForeignKey('story.id'))
    reason = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(100), default='pending')

    reporter = db.relationship('User', foreign_keys=[reporter_id], backref=db.backref('reports_made', lazy=True))
    reported_user = db.relationship('User', foreign_keys=[reported_user_id], backref=db.backref('reports_received', lazy=True))
    reported_story = db.relationship('Story', backref=db.backref('reports', lazy=True))

    def __repr__(self):
        return f'<Report {self.id} by User {self.reporter_id}>'