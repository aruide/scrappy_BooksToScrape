-- Database: bookstoscrape

-- DROP DATABASE IF EXISTS bookstoscrape;

CREATE DATABASE bookstoscrape
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Table: public.genre

-- DROP TABLE IF EXISTS public.genre;

CREATE TABLE IF NOT EXISTS public.genre
(
    id_genre integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT genre_pk PRIMARY KEY (id_genre)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.genre
    OWNER to postgres;

-- Table: public.oeuvre

-- DROP TABLE IF EXISTS public.oeuvre;

CREATE TABLE IF NOT EXISTS public.oeuvre
(
    id_oeuvre integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    title character varying COLLATE pg_catalog."default",
    description character varying COLLATE pg_catalog."default",
    rating integer,
    upc character varying COLLATE pg_catalog."default",
    prix_ht real,
    taxe real,
    nb_available integer,
    nb_review integer,
    image_url character varying COLLATE pg_catalog."default",
    genre_fk integer NOT NULL,
    CONSTRAINT oeuvre_pk PRIMARY KEY (id_oeuvre),
    CONSTRAINT genre_fk FOREIGN KEY (genre_fk)
        REFERENCES public.genre (id_genre) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.oeuvre
    OWNER to postgres;