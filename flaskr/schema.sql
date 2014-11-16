drop table if exists posts;
create table posts (
    id integer primary key autoincrement,
    titulo text not null,
    descricao text not null
);
