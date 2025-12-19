/newsbot/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── endpoints.py
│   │   └── schemas.py
│   ├── news_parser/
│   │   ├── sites.py
│   │   └── telegram.py
│   ├── telegram/
│   │   ├── bot.py
│   │   └── publisher.py
│   ├── tasks.py
│   ├── models.py
│   ├── config.py
│   └── utils.py
├── celery_worker.py
├── requirements.txt
├── README.md
└── .env