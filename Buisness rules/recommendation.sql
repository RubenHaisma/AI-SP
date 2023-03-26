DROP TABLE IF EXISTS content_recommendations CASCADE;

CREATE TABLE content_recommendations (
    profile_id varchar(255),
    product_id SERIAL PRIMARY KEY,
    category text NOT NULL,
    product_recommendation VARCHAR(255)[]
);

DROP TABLE IF EXISTS collab_recommendations CASCADE;

CREATE TABLE recommendations (
    id SERIAL NOT NULL,
    profileid varchar(255) NOT NULL,
    productid1 varchar(255) NOT NULL,
    productid2 varchar(255) NOT NULL,
    productid3 varchar(255) NOT NULL,
    productid4 varchar(255) NOT NULL,
    PRIMARY KEY (id)
);


