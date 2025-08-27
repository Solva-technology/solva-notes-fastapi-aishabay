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
925e76aea997
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.category (title, description, id, created_at, updated_at) FROM stdin;
study	hw	1	2025-08-12 12:00:00+00	2025-08-12 12:00:00+00
work	hard	2	2025-08-13 12:00:00+00	2025-08-13 12:00:00+00
hobby	random hobby	4	2025-08-18 07:24:04.22134+00	2025-08-18 07:24:30.511531+00
other	other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category other new category	6	2025-08-20 12:37:14.415381+00	2025-08-21 08:31:24.970743+00
category	category desc	7	2025-08-26 07:31:01.412266+00	2025-08-26 07:31:01.412266+00
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
note10	1	16	2025-08-26 06:12:37.043602+00	2025-08-26 06:12:37.043602+00
note17	1	17	2025-08-26 06:17:03.324382+00	2025-08-26 06:17:03.324382+00
note99	2	9	2025-08-15 12:12:04.271499+00	2025-08-26 08:56:16.198734+00
note88	2	8	2025-08-15 12:02:58.124315+00	2025-08-26 08:57:59.691916+00
string	1	18	2025-08-26 09:01:28.49854+00	2025-08-26 09:01:28.49854+00
note aisha	1	21	2025-08-26 13:14:58.972258+00	2025-08-26 13:14:58.972258+00
\.


--
-- Data for Name: notecategory; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.notecategory (note_fk, category_fk, created_at, updated_at) FROM stdin;
21	1	2025-08-26 13:14:58.972258+00	2025-08-26 13:14:58.972258+00
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.category_id_seq', 7, true);


--
-- Name: note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.note_id_seq', 21, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--
