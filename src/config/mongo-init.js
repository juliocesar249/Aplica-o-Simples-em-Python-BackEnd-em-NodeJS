db.createUser({
    user: process.env.MONGO_APP_USER,
    pwd: process.env.MONGO_APP_PASSWORD,
    roles: [
        {role: 'readWrite', db: 'jeichat'},
        {role: 'dbAdmin', db: 'jeichat'}
    ]
})

db.createCollection('mensagens')