DROP TABLE IF EXISTS device;

CREATE TABLE device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  boolean1 INTEGER NOT NULL,
  boolean2 INTEGER NOT NULL,
  integer1 INTEGER NOT NULL
);

INSERT into device (name,boolean1,boolean2,integer1) VALUES ('device1',0,1,42);