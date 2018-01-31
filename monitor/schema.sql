drop table if exists account;
create table account (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);

drop table if exists ad_account;
create table ad_account (
    id integer primary key autoincrement,
    name string not null,
    url string not null
);

drop table if exists ad_index;
create table ad_index (
    id integer primary key autoincrement,
    ad_account_id integer not null,
    view_index integer,
    like_index integer,
    share_index integer
);
