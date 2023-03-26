DROP TABLE IF EXISTS content_recommendations CASCADE;

CREATE TABLE content_recommendations (
    profile_id varchar(255),
    product_id SERIAL PRIMARY KEY,
    category text NOT NULL,
    product_recommendation VARCHAR(255)[]
);

DROP TABLE IF EXISTS collab_recommendations CASCADE;

CREATE TABLE previously_recommended (
    profileid varchar(255),
    productid varchar(255),
    category text NOT NULL,
    recommendation_timestamp timestamp without time zone DEFAULT now()
    product_recommendation VARCHAR(255)[]
);


