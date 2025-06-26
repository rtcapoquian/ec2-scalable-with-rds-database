from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import ElbApplicationLoadBalancer, InternetGateway, NATGateway
from diagrams.aws.compute import AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.general import Users

with Diagram(
    "Todo App - Network Architecture",
    show=False,
    direction="TB",
    filename="network_todo_architecture",
    outformat="png",
    graph_attr={"fontsize": "18", "fontname": "Arial Bold"},
    node_attr={"fontsize": "14", "fontname": "Arial Bold"},
):

    # External
    users = Users("Users")

    # Internet Gateway (Entry Point)
    igw = InternetGateway("Internet Gateway")

    with Cluster("AWS Region", graph_attr={"fontsize": "18", "fontname": "Arial"}):
        with Cluster("VPC", graph_attr={"fontsize": "18", "fontname": "Arial"}):
            # Tier 1 - Load Balancer (Top Tier)
            with Cluster("Tier 1 - Load Balancer", graph_attr={"fontsize": "18", "fontname": "Arial"}):
                alb = ElbApplicationLoadBalancer("ALB")
                nat = NATGateway("NAT")

            # Tier 2 - Application Layer (Middle Tier)
            with Cluster("Tier 2 - Application", graph_attr={"fontsize": "18", "fontname": "Arial"}):
                asg = AutoScaling("Auto Scaling")

            # Tier 3 - Database Layer (Bottom Tier)
            with Cluster("Tier 3 - Database", graph_attr={"fontsize": "18", "fontname": "Arial"}):
                rds_primary = RDS("Database Primary")
                rds_standby = RDS("Database Standby")

    # Traffic Flow - Top to Bottom
    users >> igw >> alb >> asg >> rds_primary

    # Database replication
    rds_primary >> Edge(label="Sync", style="dashed") >> rds_standby

    # Outbound internet access
    asg >> nat >> igw