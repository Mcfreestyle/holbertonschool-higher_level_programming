-- creates the table `unique_id` on my MySQL server
-- the `id`'s in the rows must to be unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
