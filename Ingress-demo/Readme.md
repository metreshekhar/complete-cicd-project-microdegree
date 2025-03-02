```commandline
docker build -t naruto-flask-app manojkrishnappa/naruto-flask-app:1 
```
```commandline
docker push manojkrishnappa/naruto-flask-app:1
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: naruto-flask-app
  labels:
    app: naruto-flask-app
spec:
  replicas: 2  # You can scale up the number of pods here
  selector:
    matchLabels:
      app: naruto-flask-app
  template:
    metadata:
      labels:
        app: naruto-flask-app
    spec:
      containers:
      - name: naruto-flask-app
        image: manojkrishnappa/naruto-flask-app:1
        ports:
        - containerPort: 80  # This should match the exposed port of the Flask app (80 in your case)
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"
```

service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: naruto-flask-app-service
spec:
  selector:
    app: naruto-flask-app
  ports:
    - protocol: TCP
      port: 80  # Port that the service will expose
      targetPort: 80  # Port that the container is listening on
  type: ClusterIP  # Internal service only
```

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: naruto-flask-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: naruto-flask-app.example.com  # Replace with your own domain or the Load Balancer DNS
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: naruto-flask-app-service
            port:
              number: 80
```

- commands

```commandline
kubectl apply -f deployment.yml
```

```commandline
kubectl apply -f service.yml
```
```commandline
kubectl apply -f ingress.yml
```
info: 
```commandline
root@ip-172-31-22-4:~/complete-cicd-project-microdegree/Ingress-demo/Python# kubectl apply -f deployment.yml
deployment.apps/naruto-flask-app created
root@ip-172-31-22-4:~/complete-cicd-project-microdegree/Ingress-demo/Python# kubectl apply -f service.yml
service/naruto-flask-app-service created
root@ip-172-31-22-4:~/complete-cicd-project-microdegree/Ingress-demo/Python# kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
naruto-flask-app-575496f774-lpz48   1/1     Running   0          81s
naruto-flask-app-575496f774-rpxxp   1/1     Running   0          81s
root@ip-172-31-22-4:~/complete-cicd-project-microdegree/Ingress-demo/Python# kubectl get svc
NAME                       TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes                 ClusterIP   10.100.0.1     <none>        443/TCP   66m
naruto-flask-app-service   ClusterIP   10.100.82.98   <none>        80/TCP    36s
```


```commandline
kubectl get ingress
NAME                       CLASS    HOSTS                          ADDRESS   PORTS   AGE
naruto-flask-app-ingress   <none>   naruto-flask-app.example.com             80      38s
```


If you see here address is not displying so not able create a loadbalncer
Now we are installing nginx loadbalncer to the ingress it aces as ingress-controller

This is where you get kubernetes community nginx controller 
Link: https://kubernetes.github.io/ingress-nginx/deploy/#aws

```commandline
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.0/deploy/static/provider/aws/deploy.yaml
```
```commandline
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.0/deploy/static/provider/aws/deploy.yaml
namespace/ingress-nginx created
serviceaccount/ingress-nginx created
serviceaccount/ingress-nginx-admission created
role.rbac.authorization.k8s.io/ingress-nginx created
role.rbac.authorization.k8s.io/ingress-nginx-admission created
clusterrole.rbac.authorization.k8s.io/ingress-nginx created
clusterrole.rbac.authorization.k8s.io/ingress-nginx-admission created
rolebinding.rbac.authorization.k8s.io/ingress-nginx created
rolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx created
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
configmap/ingress-nginx-controller created
service/ingress-nginx-controller created
service/ingress-nginx-controller-admission created
deployment.apps/ingress-nginx-controller created
job.batch/ingress-nginx-admission-create created
job.batch/ingress-nginx-admission-patch created
ingressclass.networking.k8s.io/nginx created
validatingwebhookconfiguration.admissionregistration.k8s.io/ingress-nginx-admission created
```
```commandline
root@ip-172-31-22-4:~/complete-cicd-project-microdegree/Ingress-demo/Python# kubectl get pods -n ingress-nginx
NAME                                       READY   STATUS    RESTARTS   AGE
ingress-nginx-admission-create-4298n       0/1     Pending   0          2m34s
ingress-nginx-admission-patch-shckl        0/1     Pending   0          2m34s
ingress-nginx-controller-cbb88bdbc-8v48z   0/1     Pending   0          2m34s
```

