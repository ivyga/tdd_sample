CREATE TABLE IF NOT EXISTS public.contact (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

INSERT INTO public.contact (first_name, last_name, email)
VALUES ('Alice', 'Smith', 'alice.smith@wwt.com');

INSERT INTO public.contact (first_name, last_name, email)
VALUES ('Bob', 'Smith', 'robert.smith@wwt.com');

INSERT INTO public.contact (first_name, last_name, email)
VALUES ('Joe', 'Smythe', 'joe.smythe@wwt.com');

INSERT INTO public.contact (first_name, last_name, email)
VALUES ('Gary', 'Ivy', 'gary.ivy@wwt.com');

