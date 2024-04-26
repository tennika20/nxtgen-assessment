select
    id as index,
    customer as customer_key,
    "First Name" as first_name,
    "Last Name" as last_name,
    company as company_name,
    city as located_city,
    country as located_country,
    phone as customer_phone,
    email as customer_email,
    subscription as subscription_date,
    website as customer_website
from
{{source('raw','customers')}}