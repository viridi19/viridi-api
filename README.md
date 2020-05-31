# viridi-api

## Deployment on IBM Cloud Kubernetes Service (IKS)

Ensure the PORT on the Dockerfile and on the yaml file is the same

To access externally on a free cluster:

- `ibmcloud ks worker ls --cluster <cluster_name>`
```
OK
ID                                                       Public IP        Private IP      Flavor   State    Status   Zone    Version
kube-br3hsalf0epirmu869ag-ericlearnin-default-0000005f   169.51.205.126   10.144.182.44   free     normal   Ready    mil01   1.16.9_1531*
```
- Get the cluster's public IP (in this case, 169.51.205.126)

- `kubectl describe service <service-name>`
```
Name:                     viridi-api
Namespace:                default
Labels:                   app=viridi-api
                          k8s-app=viridi-api
Annotations:              kubectl.kubernetes.io/last-applied-configuration:
                            {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"creationTimestamp":null,"labels":{"app":"viridi-api"},"name":"viridi-api...
Selector:                 app=viridi-api
Type:                     NodePort
IP:                       172.21.154.86
Port:                     80-8080  80/TCP
TargetPort:               8080/TCP
NodePort:                 80-8080  32587/TCP
Endpoints:                172.30.7.185:8080
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```
- Get the nodeport value (in this case, 32587)

#### Your public access point is __http://169.51.205.126:32587__
