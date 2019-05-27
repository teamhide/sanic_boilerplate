-- Auto Increment를 위한 Sequence 생성
CREATE SEQUENCE user_id_seq START 1;

-- Users 테이블 생성
CREATE TABLE users
(id bigint primary key default nextval('user_id_seq'),
email varchar(50),
password varchar(80),
nickname varchar(20),
gender varchar(2),
join_type varchar(15),
is_active boolean,
is_block boolean,
is_admin boolean,
created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP);