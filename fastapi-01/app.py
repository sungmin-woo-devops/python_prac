from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    desctiption="LMS for mananging students and coureses.",
    version="0.0.1",
    contact = {
        "name": "Sungmin Woo",
        "email": "sungminwoo.devops@gmail.com"
    },
    license_info = {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)