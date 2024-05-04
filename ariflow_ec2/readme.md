# Step By Step to deploy Airflow in EC2
* Login your aws account
* go to EC2 > Launch Instance
* name: `airflow`
* machine type: `ubuntu`
* Amazon Image (AMI): latest with free tier
* Instance Type:
    * Free tier `t2.micro` might be too slow
    * `t2.large` should be enough
* key pair: select the type of keys to use
    * if not existent go to `create new key pair`
    * name: `airflow-keypair`
    * Key pair type: `RSA`
    * file format: `.pem`
    * press `create key pair`
* Network settings:
    * check the boxes:
    * `allow HTTPS traffict from the Internet`
    * `allow HTTP traffict from the Internet`
* Storage and the rest leave as is