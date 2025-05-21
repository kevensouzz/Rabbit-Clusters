docker exec rabbit-2-disc rabbitmqctl stop_app
docker exec rabbit-2-disc rabbitmqctl reset
docker exec rabbit-2-disc rabbitmqctl join_cluster --disc rabbit@rabbit-1-disc
docker exec rabbit-2-disc rabbitmqctl start_app

docker exec rabbit-3-disc rabbitmqctl stop_app
docker exec rabbit-3-disc rabbitmqctl reset
docker exec rabbit-3-disc rabbitmqctl join_cluster --disc rabbit@rabbit-1-disc
docker exec rabbit-3-disc rabbitmqctl start_app

docker exec rabbit-1-ram rabbitmqctl stop_app
docker exec rabbit-1-ram rabbitmqctl reset
docker exec rabbit-1-ram rabbitmqctl join_cluster --ram rabbit@rabbit-1-disc
docker exec rabbit-1-ram rabbitmqctl start_app

docker exec rabbit-2-ram rabbitmqctl stop_app
docker exec rabbit-2-ram rabbitmqctl reset
docker exec rabbit-2-ram rabbitmqctl join_cluster --ram rabbit@rabbit-2-disc
docker exec rabbit-2-ram rabbitmqctl start_app

docker exec rabbit-3-ram rabbitmqctl stop_app
docker exec rabbit-3-ram rabbitmqctl reset
docker exec rabbit-3-ram rabbitmqctl join_cluster --ram rabbit@rabbit-3-disc
docker exec rabbit-3-ram rabbitmqctl start_app

# docker exec rabbit-1 rabbitmq-plugins enable rabbitmq_management

# cmd
# docker exec rabbit-1 rabbitmqctl set_policy ha-fed ".*" '{"ha-sync-mode":"automatic", "ha-mode":"all"}' --priority 1

# power shell
# docker exec rabbit-1 rabbitmqctl set_policy ha-fed '.*' '{\"ha-sync-mode\":\"automatic\", \"ha-mode\":\"all\"}' --priority 1
