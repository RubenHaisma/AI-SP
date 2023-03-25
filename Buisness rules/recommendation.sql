DROP TABLE IF EXISTS content_recommendations CASCADE;

CREATE TABLE content_recommendations (
    id SERIAL PRIMARY KEY,
    category text NOT NULL,
    product_recommendation text[] NOT NULL
);
