select
    {{
        dbt_utils.generate_surrogate_key([
        'customer_id',
        'id'])
    }} as customer_order_key,
    id as product_id,
    customer_id,
    product_name as most_purchased_product
from
{{source('raw','products')}}