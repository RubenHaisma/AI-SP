DROP TABLE IF EXISTS content_recommendations CASCADE;

CREATE TABLE content_recommendations (
    profile_id varchar(255),
    product_id SERIAL PRIMARY KEY,
    category text NOT NULL,
    product_recommendation VARCHAR(255)[]
);

DROP TABLE IF EXISTS collab_recommendations CASCADE;

CREATE TABLE collab_recommendations (
    id SERIAL NOT NULL,
    profileid varchar(255) NOT NULL,
    productid varchar(255) NOT NULL,
    score float4 NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (profileid) REFERENCES profile (id),
    FOREIGN KEY (productid) REFERENCES product (id)
);


