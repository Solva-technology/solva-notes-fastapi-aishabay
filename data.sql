--
-- PostgreSQL database dump
--

-- Dumped from database version 15.13
-- Dumped by pg_dump version 15.13

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alembic_version (version_num) FROM stdin;
fd85ad40940b
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.category (title, description, id, created_at, updated_at) FROM stdin;
study	hw	1	2025-08-12 12:00:00+00	2025-08-12 12:00:00+00
work	hard	2	2025-08-13 12:00:00+00	2025-08-13 12:00:00+00
hobby	random hobby	4	2025-08-18 07:24:04.22134+00	2025-08-18 07:24:30.511531+00
other	other new category	6	2025-08-20 12:37:14.415381+00	2025-08-20 12:37:28.263317+00
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public."user" (email, hashed_password, is_active, is_superuser, is_verified, id, created_at, updated_at) FROM stdin;
aisha@gmail.com	$argon2id$v=19$m=65536,t=3,p=4$UsWJlBlyiB015fBUYuFIGQ$DfEfnSZz4/7n6dYOJp5YIDkkF26VvblEWsUPBizpWG4	t	f	f	2	2025-08-13 06:11:38+00	2025-08-13 06:11:38+00
root@gmail.com	$argon2id$v=19$m=65536,t=3,p=4$QCs7j1OCH8AVmRFDkveaXA$mliG68OFaOpCeoHACJAoqYt/xbwuKH+JMhoKuPoQJJc	t	t	t	1	2025-08-12 14:11:09.557378+00	2025-08-12 14:11:09.557378+00
\.


--
-- Data for Name: note; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.note (text, author_id, id, created_at, updated_at) FROM stdin;
note1	1	3	2025-08-13 08:09:21.399532+00	2025-08-13 08:09:21.399532+00
note2	1	4	2025-08-13 08:09:25.677225+00	2025-08-13 08:09:25.677225+00
do hw	2	1	2025-08-12 12:00:00+00	2025-08-13 08:40:13.44091+00
note note	2	8	2025-08-15 12:02:58.124315+00	2025-08-15 12:02:58.124315+00
note9	2	9	2025-08-15 12:12:04.271499+00	2025-08-18 06:58:40.285845+00
\.


--
-- Data for Name: note_category_association; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.note_category_association (note_id, category_id) FROM stdin;
1	2
8	2
8	1
9	1
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.category_id_seq', 6, true);


--
-- Name: note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.note_id_seq', 15, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--
