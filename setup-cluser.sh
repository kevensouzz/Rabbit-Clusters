docker exec rabbit-2 rabbitmqctl stop_app
docker exec rabbit-2 rabbitmqctl reset
docker exec rabbit-2 rabbitmqctl join_cluster rabbit@rabbit-1
docker exec rabbit-2 rabbitmqctl start_app

docker exec rabbit-3 rabbitmqctl stop_app
docker exec rabbit-3 rabbitmqctl reset
docker exec rabbit-3 rabbitmqctl join_cluster rabbit@rabbit-1
docker exec rabbit-3 rabbitmqctl start_app

docker exec rabbit-1 rabbitmq-plugins enable rabbitmq_management
# docker exec rabbit-1 rabbitmqctl set_policy ha-fed ".*" '{"ha-sync-mode":"automatic", "ha-mode":"all"}' --priority 1
docker exec rabbit-1 rabbitmqctl set_policy ha-fed '.*' '{\"ha-sync-mode\":\"automatic\", \"ha-mode\":\"all\"}' --priority 1
