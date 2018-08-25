#!/usr/bin/env bash
curl -X POST http://127.0.0.1:11111/shutdown;
git pull;
mvn clean package -DskipTests=true;
nohup java -jar -spring.profiles.active=prod target/kpi-0.0.1-SNAPSHOT.jar &