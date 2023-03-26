DROP TABLE IF EXISTS content_recommendations CASCADE;

CREATE TABLE content_recommendations (
    id SERIAL PRIMARY KEY,
    category text NOT NULL,
    product_recommendation VARCHAR(255)[]
);

DROP TABLE IF EXISTS collab_recommendations CASCADE;

CREATE TABLE collab_recommendations (
    product_id varchar(255) NOT NULL,
    product_recommendation text,
    PRIMARY KEY (product_id)
);
