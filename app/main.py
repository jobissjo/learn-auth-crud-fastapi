from fastapi import  FastAPI


from app.routes import user, jobs

app = FastAPI()

app.include_router(user.router)
app.include_router(jobs.router)
