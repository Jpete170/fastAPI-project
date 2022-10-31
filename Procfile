# Modify this Procfile to fit your needs
web: prisma generate && gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app