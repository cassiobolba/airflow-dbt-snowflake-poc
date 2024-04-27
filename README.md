# airflow-dbt-snowflake-poc
This readme is incomplete so far.

## Setup Snowflake
* Setup a 30 days trial account
* Run the below commands:
```sql
USE ROLE SECURITYADMIN;

CREATE OR REPLACE ROLE DBT_ROLE COMMENT='DBT_ROLE';
GRANT ROLE DBT_ROLE TO ROLE SYSADMIN;

CREATE OR REPLACE USER DBT_USER 
  PASSWORD='<YOUR PASS>'
	DEFAULT_ROLE=dbt_DEV_ROLE
	DEFAULT_WAREHOUSE=dbt_WH
	COMMENT='dbt User';
    
GRANT ROLE DBT_ROLE TO USER DBT_USER;

-- Grant privileges to role
USE ROLE ACCOUNTADMIN;

GRANT CREATE DATABASE ON ACCOUNT TO ROLE DBT_ROLE;

/*---------------------------------------------------------------------------
Next we will create a virtual warehouse that will be used
---------------------------------------------------------------------------*/
USE ROLE SYSADMIN;

--Create Warehouse for dbt work
CREATE OR REPLACE WAREHOUSE DBT_WH
  WITH WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 120
  AUTO_RESUME = true
  INITIALLY_SUSPENDED = TRUE;

GRANT ALL ON WAREHOUSE DBT_WH TO ROLE DBT_ROLE;
```
* Login with the recently created user and run this sql:
```
CREATE OR REPLACE DATABASE DEMO_DBT
```
## Run DBT docs
1 - Add the port exposuser in the worker deployment like this below, and rebuild the container
```yml
  airflow-worker:
    <<: *airflow-common
    command: celery worker
    ports:
      - 8081:8081
```
2 - enter in the worker container, via docker desktop or exec into it
3 - to exec into into it
  * run `docker ps`
  * get the container id from the image corresponding to the worker, should be something like `511926b065ed`
  * then run `docker exec -it  511926b065ed bash`
4 - cd to the dbt folder ( in my case, had to go back 2 folders with  `cd ..` till find the dbt folder)
5 - from inside the dbt folder run `dbt docs generate` and then `dbt docs serve --port 8081`
6 - docs should be accesible in the link


## Help
### Get dbt up and running from the command line on a MacBook with an M1 chip - Error for Mac Users
https://discourse.getdbt.com/t/get-dbt-up-and-running-from-the-command-line-on-a-macbook-with-an-m1-chip/2908/2

### Compilation Error
```
[2024-04-26, 13:15:11 UTC] {subprocess.py:93} INFO -   dbt found 1 package(s) specified in packages.yml, but only 0 package(s) installed in dbt_packages. Run "dbt deps" to install package dependencies.
```
Need to run `dbt deps` to install deps, because container was destroyed and the state was lost:
* start docker
* run `docker ps`
* get the container id from the image corresponding to the worker, should be something like `511926b065ed`
* then run `docker exec -it  511926b065ed bash`
* find enter in the dbt folder. If not finding cd out with `cd ..` then `ls` to find the dbt folder and cd into it
* run `dbt deps`