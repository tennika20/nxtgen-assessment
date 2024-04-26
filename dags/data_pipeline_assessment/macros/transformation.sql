{% macro uppercase_customer_names(column_name) %}
    UPPER({{ column_name }})
{% endmacro %}