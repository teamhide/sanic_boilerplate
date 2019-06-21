#!/bin/bash
echo "[*] Deploy Start"
aws s3 cp test_appspec.yaml s3://BUCKET_NAME_HERE/appspec.yaml
echo "[*] Upload appspec.yaml to S3 Done"
sleep 3
aws deploy \
create-deployment \
--application-name CODEDEPLOY_APPLICATION_NAME_HERE \
--deployment-group-name CODEDEPLOY_DEPLOYMENT_GROUP_NAME_HERE \
--s3-location bucket=BUCKET_NAME_HERE,bundleType=yaml,key=appspec.yaml
echo "[*] Deploy Done"