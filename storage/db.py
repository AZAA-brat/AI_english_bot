import aiosqlite

DB_PATH = "databases.db"
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript("""
        CREATE TABLE IF NOT EXISTS users(
        telegram_id BIGINT PRIMARY KEY,
        mode TEXT NOT NULL DEFAULT 'Translate' CHECK( mode IN ('Translate', 'Grammar', 'Writing')),
        language TEXT NOT NULL DEFAULT 'ru > en' CHECK( language IN ('ru > en', 'en > ru')),
        name TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id BIGINT NOT NULL REFERENCES users(telegram_id),
        role TEXT NOT NULL CHECK( role IN ('User', 'Bot')),
        text TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """
        )
        await db.commit()

async def conn_db():
    db = await aiosqlite.connect(DB_PATH)
    await db.execute("PRAGMA foreign_keys = ON")
    return db

async def add_user(telegram_id, name):
    db = await conn_db()
    try:
        await db.execute("INSERT OR IGNORE INTO users(telegram_id, name) VALUES (?, ?);", (telegram_id, name,))
        await db.commit()
    finally:
        await db.close()

async def get_user(telegram_id):
    db = await conn_db()
    try:
        cursor = await db.execute("SELECT * FROM users WHERE telegram_id = ? ", (telegram_id,))
        row = await cursor.fetchone()
        return row
    finally:
        await db.close()

async def update_user_settings(telegram_id, mode, language):
    db = await conn_db()
    try:
        await db.execute("UPDATE users SET mode = ?, language = ? WHERE telegram_id = ?;", (mode, language, telegram_id,))
        await db.commit()
    finally:
        await db.close()

async def save_message(telegram_id, role, text):
    db = await conn_db()
    try:
        await db.execute("INSERT INTO messages(user_id, role, text) VALUES (?, ?, ?);", (telegram_id, role, text,))
        await db.commit()
    finally:
        await db.close()

async def get_messages(user_id):
    limit = 10
    db = await conn_db()
    try:
        cursor = await db.execute("SELECT * FROM messages WHERE user_id = ? ORDER BY created_at DESC LIMIT ?;", (user_id, limit,))
        row = await cursor.fetchall()
        return row[::-1]
    finally:
        await db.close()
