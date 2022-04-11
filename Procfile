release: prisma generate
web: gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app
