SELECT  m.full_name, c.full_name, c.city, m.city
FROM 'order' o JOIN manager m ON o.manager_id = m.manager_id
                JOIN customer c ON m.manager_id = c.manager_id
WHERE m.city != c.city
GROUP BY m.full_name, c.full_name