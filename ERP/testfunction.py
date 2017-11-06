"SELECT appointment_id, a.customer_id, customer_name, job, time_appointment, estimated_time, appointment_name, content, status FROM clinic_calendarappointment a, clinic_customer b WHERE date_appointment = '{0}' AND a.customer_id = b.customer_id ORDER BY status"
    """SELECT
              appointment_id
            , customer_id
            , customer_name
            , customer_phone_number
            , appointment_time
            , appointment_name
            , appointment_content
            , appointment_status
        FROM
              clinic_customer customer
            , clinic_appointment appoinment
        WHERE
                date_appointment = '{0}'
            AND customer.customer_id = appoinment.customer_id
            AND appointment_delete_flag = '0'
    """.format(current_date)

    """
        SELECT
              appointment_id
            , user_name
            , appointment_date
            ,


    """
print(dm)