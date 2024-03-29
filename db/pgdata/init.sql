CREATE TABLE IF NOT EXISTS NameUsage (
	ID TEXT PRIMARY KEY,
	sourceID TEXT DEFAULT NULL,
	parentID TEXT DEFAULT NULL,
	basionymID TEXT DEFAULT NULL,
	"status" VARCHAR DEFAULT NULL,
	scientificName TEXT DEFAULT NULL,
	authorship TEXT DEFAULT NULL,
	"rank" VARCHAR DEFAULT NULL,
	notho TEXT DEFAULT NULL,
	uninomial VARCHAR DEFAULT NULL,
	genericName TEXT DEFAULT NULL,
	infragenericEpithet VARCHAR DEFAULT NULL,
	specificEpithet VARCHAR DEFAULT NULL,
	infraspecificEpithet VARCHAR DEFAULT NULL,
	cultivarEpithet VARCHAR DEFAULT NULL,
	namePhrase TEXT DEFAULT NULL,
	nameReferenceID TEXT DEFAULT NULL,
	publishedInYear INT DEFAULT NULL,
	publishedInPage TEXT DEFAULT NULL,
	publishedInPageLink TEXT DEFAULT NULL,
	code VARCHAR DEFAULT NULL,
	nameStatus VARCHAR DEFAULT NULL,
	accordingToID TEXT DEFAULT NULL,
	accordingToPage TEXT DEFAULT NULL,
	accordingToPageLink TEXT DEFAULT NULL,
	referenceID TEXT DEFAULT NULL,
	scrutinizer TEXT DEFAULT NULL,
	scrutinizerID TEXT DEFAULT NULL,
	scrutinizerDate VARCHAR DEFAULT NULL,
	extinct BOOLEAN DEFAULT NULL,
	temporalRangeStart VARCHAR DEFAULT NULL,
	temporalRangeEnd VARCHAR DEFAULT NULL,
	environment VARCHAR DEFAULT NULL,
	species TEXT DEFAULT NULL,
	section TEXT DEFAULT NULL,
	subgenus TEXT DEFAULT NULL,
	genus TEXT DEFAULT NULL,
	subtribe TEXT DEFAULT NULL,
	tribe TEXT DEFAULT NULL,
	subfamily TEXT DEFAULT NULL,
	family TEXT DEFAULT NULL,
	superfamily TEXT DEFAULT NULL,
	suborder TEXT DEFAULT NULL,
	"order" TEXT DEFAULT NULL ,
	subclass TEXT DEFAULT NULL,
	"class" TEXT DEFAULT NULL,
	subphylum TEXT DEFAULT NULL,
	phylum TEXT DEFAULT NULL,
	kingdom TEXT DEFAULT NULL,
	sequenceIndex INT DEFAULT NULL,
	branchLength INT DEFAULT NULL,
	link TEXT DEFAULT NULL,
	nameRemarks TEXT DEFAULT NULL,
	remarks TEXT DEFAULT NULL
);


CREATE TABLE IF NOT EXISTS Findings (
	ID SERIAL PRIMARY KEY,
	speciesID TEXT NOT NULL,
	researcherEmail TEXT NOT NULL,
	findingDate TIMESTAMP NOT NULL,
	"location" TEXT NOT NULL,
	notes TEXT
);


COPY NameUsage FROM '/var/lib/postgresql/tsvs/NameUsage.tsv' DELIMITER E'\t' CSV HEADER;