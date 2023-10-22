SELECT c.full_name, m.full_name, o.purchase_amount, o.date
FROM customer c JOIN manager m ON c.manager_id = m.manager_id
                JOIN "order" o ON c.customer_id = o.customer_id
