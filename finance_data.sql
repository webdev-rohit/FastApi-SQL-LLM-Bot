--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-07-12 22:07:31

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 24591)
-- Name: finance_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.finance_data (
    gender character varying(255),
    age character varying(255),
    stock_market character varying(255),
    factor character varying(255),
    purpose character varying(255),
    duration character varying(255),
    savings_objectives character varying(255)
);


ALTER TABLE public.finance_data OWNER TO postgres;

--
-- TOC entry 4830 (class 0 OID 24591)
-- Dependencies: 215
-- Data for Name: finance_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.finance_data (gender, age, stock_market, factor, purpose, duration, savings_objectives) FROM stdin;
Female	34	Yes	Returns	Wealth Creation	1-3 years	Retirement Plan
Female	23	No	Locking Period	Wealth Creation	More than 5 years	Health Care
Male	30	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Male	22	Yes	Returns	Wealth Creation	Less than 1 year	Retirement Plan
Female	24	No	Returns	Wealth Creation	Less than 1 year	Retirement Plan
Female	24	No	Risk	Wealth Creation	1-3 years	Retirement Plan
Female	27	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Male	21	Yes	Risk	Wealth Creation	3-5 years	Retirement Plan
Male	35	Yes	Returns	Savings for Future	1-3 years	Retirement Plan
Male	31	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Female	35	Yes	Risk	Savings for Future	3-5 years	Retirement Plan
Male	29	Yes	Risk	Wealth Creation	1-3 years	Retirement Plan
Female	21	No	Returns	Savings for Future	1-3 years	Education
Female	28	Yes	Returns	Wealth Creation	1-3 years	Retirement Plan
Female	25	Yes	Returns	Wealth Creation	1-3 years	Health Care
Male	27	Yes	Returns	Wealth Creation	1-3 years	Health Care
Female	28	Yes	Risk	Wealth Creation	1-3 years	Health Care
Male	27	Yes	Returns	Wealth Creation	1-3 years	Retirement Plan
Male	29	Yes	Risk	Wealth Creation	1-3 years	Retirement Plan
Male	26	Yes	Risk	Wealth Creation	3-5 years	Health Care
Male	29	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Female	24	Yes	Risk	Wealth Creation	3-5 years	Health Care
Male	27	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Male	25	Yes	Risk	Savings for Future	3-5 years	Health Care
Female	26	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Female	32	Yes	Risk	Wealth Creation	3-5 years	Retirement Plan
Male	26	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Male	31	Yes	Risk	Savings for Future	1-3 years	Health Care
Male	29	Yes	Returns	Wealth Creation	1-3 years	Retirement Plan
Female	34	Yes	Returns	Returns	3-5 years	Retirement Plan
Male	27	No	Returns	Wealth Creation	1-3 years	Education
Female	31	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
Male	27	Yes	Returns	Wealth Creation	3-5 years	Health Care
Male	26	Yes	Returns	Returns	1-3 years	Education
Male	27	Yes	Returns	Wealth Creation	1-3 years	Health Care
Male	30	Yes	Risk	Wealth Creation	3-5 years	Health Care
Male	30	Yes	Returns	Wealth Creation	1-3 years	Retirement Plan
Male	25	Yes	Risk	Savings for Future	3-5 years	Health Care
Male	31	Yes	Risk	Wealth Creation	1-3 years	Health Care
Male	29	Yes	Returns	Wealth Creation	3-5 years	Retirement Plan
\.


-- Completed on 2024-07-12 22:07:32

--
-- PostgreSQL database dump complete
--

