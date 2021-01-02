create external table Yelp_data(id string, date_stamp string, reviews string, business_id string,stars float) row format delimited fields terminated by ',' LINES TERMINATED BY '\n' location  '/user/ss13449/project/cleaned_data/data_yelp/';

create external table Yelp_business_data(business_id string, business_name string, city string, state string) row format delimited fields terminated by ',' LINES TERMINATED BY '\n' location  '/user/ss13449/project/cleaned_data/data_yelp_business/';

create external table Yelp_review(id string, date_stamp date,reviews string,business_id string,business_name string,stars float,city string,state string) STORED AS TEXTFILE LOCATION 'hdfs://dumbo/user/ss13449/project/cleaned_data/tabledata/yelp';

INSERT OVERWRITE TABLE Yelp_review select id, cast(to_date(from_unixtime(unix_timestamp(date_stamp, 'dd-MM-yyyy'))) as date),reviews,yelp_data.business_id,yelp_business_data.business_name,stars,city,state from yelp_data JOIN yelp_business_data ON yelp_data.business_id=yelp_business_data.business_id;
