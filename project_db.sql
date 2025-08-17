BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "jobs" (
	"id"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	"company"	TEXT NOT NULL,
	"location"	TEXT NOT NULL,
	"about_company"	TEXT NOT NULL,
	"company_website" TEXT NOT NULL,
	"responsibilities"	TEXT NOT NULL,
	"requirements"	TEXT NOT NULL,
	"salary"	TEXT,
	"currency"	TEXT DEFAULT 'MK',
	"open_until" TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "applications" (
	"id"	INTEGER NOT NULL,
	"job_id"	INTEGER NOT NULL,
	"fullname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"linkedin_url"	TEXT,
	"education_bg"	TEXT,
	"work_exp"	TEXT,
	"resume_url"	TEXT,
	"sent_on"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("job_id") REFERENCES "jobs"("id")
);
CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	INTEGER NOT NULL UNIQUE,
	"fullname"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"password"	TEXT NOT NULL DEFAULT 'password',
	"user_role"	TEXT NOT NULL DEFAULT 'User',
	PRIMARY KEY("user_id" AUTOINCREMENT)
);
INSERT INTO "users" VALUES (1,'0xNone2Deep','oxnone2deep','none2deep@proton.me','gAAAAABkRsduBwUMMMaXPN55NpF2dmSdmmywlJAwUkWYSyuvtzoURgBnMF9hsCke2rgZzr29Q5Cfl7ADYKuS0OmEhOwDU9U2Ew==','Admin');
COMMIT;
