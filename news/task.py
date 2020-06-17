from celery import task

@task
def mul(x,y):
    return x * y