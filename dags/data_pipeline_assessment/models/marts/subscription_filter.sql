select
    customer_data.index,
    customer_data.customer_key,
    product_data.most_purchased_product,
    {{ uppercase_customer_names('customer_data.first_name') }} as first_name,
    {{ uppercase_customer_names('customer_data.last_name') }} as last_name,
    customer_data.customer_email,
    customer_data.subscription_date,
    customer_data.located_country,
    customer_data.located_city
from
    {{ ref('stg_model_customers') }} as customer_data
join
    {{ ref('stg_model_products') }} as product_data
on
    customer_data.index =  product_data.customer_id
where
    SUBSTRING(customer_data.subscription_date, 1, 4) != '2021'
order by
    customer_data.index