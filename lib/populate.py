from main import Post, User, Session
local_session=Session()


# new_user=User(
#     username="testuser",
#     email='testuser@gmail.com'
# )

# local_session.add(new_user)
# local_session.commit()
posts=[
    {
        "title":"Learn Django",
        "content":"Lorem ipsum"
    },
     {
        "title":"Learn Java",
        "content":"Lorem ipsum"
    },
      {
        "title":"Learn javascript",
        "content":"Lorem ipsum"
    },
 {
        "title":"Learn css",
        "content":"Lorem ipsum"
    }, {
        "title":"Learn HTML",
        "content":"Lorem ipsum"
    }


]

user=local_session.query(User).filter(User.id==1).first()


for post in posts:
    
    new_post=Post(
        title=post['title'],
        content=post['content'],
        author=user
        )
    local_session.add(new_post)
    local_session.commit()
    
    print(f"Post created____ {post['title']}")

