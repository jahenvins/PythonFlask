BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "form" (
	"pID"	INTEGER NOT NULL,
	"name"	TEXT,
	"theme"	TEXT,
	"PhoneNo"	NUMERIC,
	"sex"	TEXT,
	"Age"	NUMERIC,
	"food"	TEXT,
	"location"	TEXT,
	"date"	date,
	"stime"	time,
	"etime"	t,
	"req"	TEXT,
	"guestno"	NUMERIC,
	PRIMARY KEY("pID" AUTOINCREMENT)
);
INSERT INTO "form" VALUES (467,'q','w',123,'Female',21,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
COMMIT;
