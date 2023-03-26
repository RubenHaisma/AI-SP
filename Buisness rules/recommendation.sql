DROP TABLE IF EXISTS content_recommendations CASCADE;

CREATE TABLE content_recommendations (
    profile_id varchar(255),
    product_id SERIAL PRIMARY KEY,
    category text NOT NULL,
    product_recommendation VARCHAR(255)[]
);

DROP TABLE IF EXISTS collab_recommendations CASCADE;

CREATE TABLE collab_recommendations (
    profile_id varchar(255),
    product_id varchar(255),
    category text,
    recommendations_timestamp timestamp NOT NULL,
    product_recommendation text,
    PRIMARY KEY (product_id)
);

