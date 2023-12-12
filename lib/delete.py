from main import Post, User, Session

local_session= Session()

user_to_delete= local_session.query(User).filter(User.id==1).first()

local_session.delete(user_to_delete)
local_session.commit()

all_posts= local_session.query(Post).all()

all_users=local_session.query(User).all()



print(all_posts)
print(all_users)