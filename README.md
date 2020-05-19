# Googlesheet REST API
This repository creates Docker image which can be deployed on Docker, Kubernetes (GKE) and Google  Cloud Run.

## Docker

- Create Service Account in GCP
- Go to your spreadsheet and share it with a client_email from the step above.
- Create a folder credentials/<file_name>.json
- Run following command to run docker container
```bash
docker run -v $PWD/credentials:/app/credentials -p 8080:8080 vikramshinde/cloud-run-googlesheet:latest
```


## Kubernets

- Create Service account in GCP
- Create Kubernetes cluster in GKE
- Create Kubernetes Secrete 
```bash 
kubectl create secret generic googlesheet-key --from-file=key.json=PATH-TO-KEY-FILE.json
```
- Deploy the Deployment and Service in Kubernetes
```bash
kubectl create -f kubernetes/.
```  

##Cloud Run


The cloudbuild.yaml file will trigger the cloudrun.
