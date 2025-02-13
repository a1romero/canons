## Machine Reading Test Set
This folder contains extracted data from the database in .csv format. Filenames are organized by their ID in the database and a name for the anthology.

### How to get more data
The data is extracted from the anthologies database. To gain the data you need to run this SQL query:

```
select
    dw2.title as "Work",
    da."name" as "Author",
    dw.work_id,
    dw.anthology_id,
    dw.toc_page as "Page Number"
from
    public.data_work dw2
inner join public.data_work_authors dwa on dw2.id = dwa.work_id
inner join public.data_author da on dwa.author_id = da.id
inner join public.data_workinanthology dw on dw2.id = dw.work_id
where dw.anthology_id = ANTHOLOGY_ID_HERE
order by dw.toc_page ASC;
```

Then save the data and upload it to this folder. We did this in DBeaver.

You can get the anthology IDs with the SQL script:

```
select *
from data_anthology da
order by title asc;
```
