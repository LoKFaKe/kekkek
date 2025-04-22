-- Таблицы для расписания
CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE schedule (
    id INTEGER PRIMARY KEY,
    group_id INTEGER,
    subject TEXT NOT NULL,
    day TEXT NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Таблицы для магазина
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);