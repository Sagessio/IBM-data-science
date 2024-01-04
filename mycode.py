select * from pn_profession where phone_number in (select distinct vendor_contact_number from (select distinct a.vendor_contact_number, a.vendor_name, b.need from pn_need_history a
inner join pn_jobdetails b on a.need_id = b.job_id
where a.job_status in ('In Progress')
and date(a.last_modified) between ('2020-10-02') and (Current_date)) as foo)


select distinct a.vendor_contact_number, a.vendor_name, b.need from pn_need_history a
inner join pn_jobdetails b on a.need_id = b.job_id
where a.job_status in ('In Progress')
and date(a.last_modified) between ('2020-10-02') and (Current_date)


select * from pn_profession where phone_number in (select distinct vendor_contact_number from (select distinct a.vendor_contact_number, a.vendor_name, b.need from pn_need_history a
inner join pn_jobdetails b on a.need_id = b.job_id
where a.job_status in ('In Progress')
and date(a.last_modified) between ('2020-10-02') and (Current_date)) as foo)


select phone_number, profession, skill1, skill2 from pn_profession where phone_number in (select distinct vendor_contact_number from (select distinct a.vendor_contact_number, a.vendor_name, b.need from pn_need_history a
inner join pn_jobdetails b on a.need_id = b.job_id
where a.job_status in ('In Progress')
and date(a.last_modified) between ('2020-10-02') and (Current_date)) as foo)


select job_id, need from pn_jobdetails
where date(date) between ('2020-10-02') and (Current_date)

select a.vendor_contact_number, a.vendor_name, a.need_id, b.need from pn_need_history a
inner join pn_jobdetails b on a.need_id = b.job_id
where a.job_status in ('In Progress')
and date(a.last_modified) between ('2020-10-02') and (Current_date)




