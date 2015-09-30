CREATE OR REPLACE PROCEDURE STG.PRC_LOAD_PREPAID_VOICE_NEW (p_thread_no number)
as

v_thread_no varchar2(100) := lpad(p_thread_no, 2, '0');
v_sql varchar2(1000);

v_status varchar2(100);

v_message varchar2(100);

v_start_date date;



begin


 v_start_date := sysdate;

 /*
 execute immediate 'truncate table ldr_prepaid_voice_cdr_'||v_thread_no;

 v_sql :='insert /*+ append */ /*into ldr_prepaid_voice_cdr_'||v_thread_no||' select * from
         ext_prepaid_voice_cdr_'||v_thread_no;


 execute immediate v_sql;

   commit;
*/
  v_status := 'SUCCESS';

  v_message := 'COMPLETED SUCCESSFULLY';

  insert into prepaid_voice_thread_control(thread_no, status, message, start_date, end_date, duration)
    values (p_thread_no, v_status, v_message, v_start_date, sysdate, (sysdate - v_start_date) * 24 * 3600);

  commit;

exception when others then

  v_message := substr(sqlerrm,1,200);

  v_status := 'FAILURE';

  insert into prepaid_voice_thread_control(thread_no, status, message, start_date, end_date, duration)
    values (p_thread_no, v_status, v_message, v_start_date, sysdate, (sysdate - v_start_date) * 24 * 3600);

  commit;

end;
/
