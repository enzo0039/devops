## Prometheus x Grafana x Flask

Déploiement via docker-compose d'une application Flask utilisant Prometheus pour les métriques et Grafana pour le dashboard.

### Installation des dépendances

```bash
pip install -r flask-app/requirements.txt
```

### Configuration et exécution du docker-compose

```bash
docker compose up -d
```

### Accès

* API: http://localhost:5000/
* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000 `[username: admin, password: pass@123]`
