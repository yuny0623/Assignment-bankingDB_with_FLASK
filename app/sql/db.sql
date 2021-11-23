drop table account_record; 
drop table card;
drop table user_account;
drop table user; 

create table user(
	user_SSN 		varchar(26) unique,
    user_name 		varchar(20) not null ,
    user_address 	varchar(30),
    user_birth 		varchar(20),
    user_email 		varchar(30) unique,
    user_phone 		varchar(20) unique,
	user_job 		varchar(20),
    constraint user_pk1 primary key (user_name, user_phone, user_email, user_SSN) 
);

create table user_account(
	account_id varchar(10), 
    account_class varchar(10) not null, 
    account_left numeric(15) not null,
    card_register numeric(1), 
    account_opendate varchar(20) not null, 
	account_user_name varchar(20), 
    account_user_phone varchar(20), 
    account_user_email varchar(30), 
    account_user_SSN varchar(26), 
    constraint account_id_pk1 primary key(account_id), 
    constraint account_left_uc1 unique(account_left), 
    constraint account_name_fk1 foreign key(account_user_name) references user(user_name),
    constraint account_phone_fk2 foreign key(account_user_phone) references user(user_phone),
    constraint account_email_fk3 foreign key(account_user_email) references user(user_email),
    constraint account_user_SSN_fk4 foreign key(account_user_SSN) references user(user_SSN)
);

create table card(
	card_id varchar(10),
    card_register_date varchar(20) not null,
    card_limit numeric(10),
    card_used_date varchar(20),
    card_class varchar(20) not null, 
    card_user_SSN varchar(26),
    card_user_account_id varchar(10),
    constraint card_id_pk1 primary key(card_id),
    constraint card_user_SSN_fk1 foreign key(card_user_SSN) references user(user_SSN), 
	constraint card_user_account_id_fk2 foreign key(card_user_account_id) references user_account(account_id)
);

create table account_record(
	account_id varchar(10), 
    banking_date varchar(40),
    record_number numeric(10),
    account_class varchar(10), 
	account_content varchar(20), 
    record_amount numeric(10) not null, 
    account_left numeric(15), 
    constraint account_user_record_pk1 primary key(account_id, banking_date, record_number),
    constraint account_record_account_id_fk1 foreign key(account_id) references user_account(account_id)
);


insert into user(user_SSN, user_name, user_address, user_birth, user_email, user_phone, user_job) values('950806-1813116', 'thanos', 'ace street', '950806', 'thanos@gmail.com', '010-1113-5559', 'programmer');
insert into user(user_SSN, user_name, user_address, user_birth, user_email, user_phone, user_job) values('990307-1234521', 'Christian Bale', 'tolkin street', '990307', 'Christian Bale@gmail.com', '010-7456-1254', 'hunter');
insert into user(user_SSN, user_name, user_address, user_birth, user_email, user_phone, user_job) values('021225-18623324', 'Kendall Jenner', 'max street', '021225', 'Kendall Jenner@gmail.com', '010-7733-1289', 'model');
insert into user(user_SSN, user_name, user_address, user_birth, user_email, user_phone, user_job) values('031125-1234634', 'trump', 'western village', '031125', 'trump@gmail.com', '010-4137-4852', 'president');
insert into user(user_SSN, user_name, user_address, user_birth, user_email, user_phone, user_job) values('981120-8653535', 'richard feynman', 'texas', '981120', 'richardfeynman@gmail.com', '010-4796-4885', 'student');

insert into user_account(account_id, account_class, account_left, card_register, account_opendate, account_user_name, account_user_phone, account_user_email, account_user_SSN) 
values ('acc_1', 'checking', 1354541, 0, '2021-09-12', 'thanos', '010-1113-5559', 'thanos@gmail.com', '950806-1813116');
insert into user_account(account_id, account_class, account_left, card_register, account_opendate, account_user_name, account_user_phone, account_user_email, account_user_SSN) 
values ('acc_2', 'saving', 9906421544, 1, '1990-07-08', 'Christian Bale', '010-7456-1254','Christian Bale@gmail.com', '990307-1234521');
insert into user_account(account_id, account_class, account_left, card_register, account_opendate, account_user_name, account_user_phone, account_user_email, account_user_SSN) 
values ('acc_3', 'saving', 987613548, 1, '2016-05-11', 'Kendall Jenner', '010-7733-1289', 'Kendall Jenner@gmail.com', '021225-18623324');
insert into user_account(account_id, account_class, account_left, card_register, account_opendate, account_user_name, account_user_phone, account_user_email, account_user_SSN) 
values ('acc_4', 'checking', 1000031015010, 1, '1980-12-11', 'trump', '010-4137-4852', 'trump@gmail.com','031125-1234634');
insert into user_account(account_id, account_class, account_left, card_register, account_opendate, account_user_name, account_user_phone, account_user_email, account_user_SSN) 
values ('acc_5', 'saving', 123000, 0, '1969-9-12', 'richard feynman', '010-4796-4885','richardfeynman@gmail.com', '981120-8653535');

insert into card(card_id, card_register_date, card_limit, card_used_date, card_class, card_user_SSN, card_user_account_id) 
values('card_1', '2000-04-22', 4000000, '2021-11-11', 'credit', '990307-1234521', 'acc_2' );
insert into card(card_id, card_register_date, card_limit, card_used_date, card_class, card_user_SSN, card_user_account_id) 
values('card_2', '2018-09-10', 900000, '2021-11-22', 'credit', '021225-18623324', 'acc_3' );
insert into card(card_id, card_register_date, card_limit, card_used_date, card_class, card_user_SSN, card_user_account_id) 
values('card_3', '2000-04-22', 100000000, '1981-03-07', 'credit', '031125-1234634', 'acc_4' );

insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left) 
values('acc_2', '2021-11-19', 1,'saving', 'save salary', 300000, 9906421544); 
insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left) 
values('acc_2', '2021-10-31', 2,'saving', 'save salary', 300000, 9906421544); 
insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left) 
values('acc_3', '2021-11-07', 3,'saving', 'save salary', 70000000, 987613548); 
insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left) 
values('acc_4', '2021-10-23', 4,'checking', 'change car', 10000000, 1000031015010); 
insert into account_record(account_id, banking_date, record_number, account_class, account_content, record_amount, account_left) 
values('acc_2', '2021-10-17', 5,'saving', 'save salary', 300000, 9906721544); 

commit; 
