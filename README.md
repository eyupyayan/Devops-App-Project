# DevOps End-to-End Local Project

Et komplett **lokalt DevOps-prosjekt** som demonstrerer hele flyten fra applikasjon → container → Kubernetes → GitOps → monitoring.

Prosjektet er laget for læring og eksperimentering, ikke produksjon.
Alt kjører lokalt med **Docker Desktop + Kubernetes**.

---

## 🎯 Mål

Lære praktisk bruk av:

* Docker
* Kubernetes
* Helm
* ArgoCD (GitOps)
* Prometheus
* Grafana

Gjennom et sammenhengende prosjekt hvor samme app deployes, skaleres og monitoreres.

---

## Arkitektur – Oversikt

```
Python App
   ↓
Docker Image (DockerHub)
   ↓
Kubernetes Cluster (lokal)
   ↓
Helm Chart (dev / prod)
   ↓
ArgoCD (GitOps deploy)
   ↓
Prometheus (metrics)
   ↓
Grafana (dashboards)
```

---

# Fase 1 – App + Container

## Hva som ble gjort

* Laget en Python FastAPI-app med flere filer
* Strukturert prosjektmappe realistisk
* Laget Dockerfile
* Bygget Docker image
* Kjørt container lokalt
* Pushet image til DockerHub
* Verifisert image fra “scratch”

## App-struktur

```
devops-app/
 ├─ app/
 │   ├─ main.py
 │   ├─ routes.py
 │   └─ utils.py
 ├─ requirements.txt
 ├─ Dockerfile
 └─ README.md
```

## Viktige konsepter

* **Image vs Container**
* **Docker layers & caching**
* **Dependency pinning**
* **Port mapping**
* **Reproduserbarhet**

---

# Fase 2 – Kubernetes + Helm + ArgoCD

## Hva som ble gjort

* Opprettet Helm chart for appen
* Deployment, Service, ConfigMap og HPA inkludert
* Dev og Prod values
* Separate namespaces
* To Helm releases:

  * `app-dev`
  * `app-prod`
* Installert ArgoCD
* Knyttet Helm chart til ArgoCD via GitOps

---

## Helm Chart Struktur

```
charts/devops-app/
 ├─ Chart.yaml
 ├─ values.yaml
 ├─ env/
 │   ├─ values-dev.yaml
 │   └─ values-prod.yaml
 └─ templates/
     ├─ deployment.yaml
     ├─ service.yaml
     ├─ configmap.yaml
     ├─ hpa.yaml
     └─ _helpers.tpl
```

---

## Namespaces

| Namespace | Formål            |
| --------- | ----------------- |
| apps-dev  | Dev miljø         |
| apps-prod | Prod miljø        |
| argocd    | GitOps controller |
| monitor   | Monitoring stack  |

---

## GitOps Flyt

1. Endring pushes til Git
2. ArgoCD oppdager diff
3. ArgoCD deployer automatisk
4. Cluster state = Git state

---

# Fase 3 – Monitoring

## Hva som ble gjort

* Opprettet `monitor` namespace
* Installert Prometheus
* Installert Grafana
* Eksponert metrics fra app
* Laget enkelt dashboard

---

## Monitoring Arkitektur

```
App Pods → /metrics
   ↓
Prometheus scrapes metrics
   ↓
Grafana visualiserer data
```

---

## Eksempler på Metrics

* HTTP requests
* Response time
* CPU usage
* Pod count
* Uptime

---

# Hvordan kjøre lokalt

## Krav

* Docker Desktop
* Kubernetes aktivert
* Helm installert
* kubectl
* Git

---

## Bygg og push image

```bash
docker build -t <user>/devops-app:1.0 .
docker push <user>/devops-app:1.0
```

---

## Deploy via Helm (manuelt)

```bash
helm upgrade --install app-dev charts/devops-app -n apps-dev -f env/values-dev.yaml
helm upgrade --install app-prod charts/devops-app -n apps-prod -f env/values-prod.yaml
```

---

## ArgoCD UI

```bash
kubectl -n argocd port-forward svc/argocd-server 8080:443
```

Åpne:
[https://localhost:8080](https://localhost:8080)

---

## Grafana UI

```bash
kubectl -n monitor port-forward svc/grafana 3000:3000
```

Åpne:
[http://localhost:3000](http://localhost:3000)

---

# Hva dette prosjektet demonstrerer

* Containerisering
* Infrastructure as Code
* GitOps workflow
* Autoskalering
* Miljø-separasjon
* Observability
* Reproduserbar lokal DevOps-stack

---

# Begrensninger (Bevisste)

* Ingen cloud-spesifikke tjenester
* Ingen enterprise-security
* Ingen ingress/load balancer
* Fokus på læring, ikke produksjon

---

# Neste steg (valgfritt)

* Legg til Ingress
* CI pipeline
* Canary deploy
* Alerting i Grafana
* Secrets management

---

**Formål:**
Dette repoet er laget som en komplett læringsreise gjennom moderne DevOps-verktøy i miniatyr – alt lokalt, alt forståelig, alt kontrollerbart.
