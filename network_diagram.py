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
    node_attr={"fontsize": "16", "fontname": "Arial Bold", "style": "filled", "fillcolor": "#e6f0ff", "color": "#222244"},
):
    # External
    users = Users("Users")

    # Internet Gateway (Entry Point)
    igw = InternetGateway("Internet Gateway")

    with Cluster("AWS Region", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
        with Cluster("VPC", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
            with Cluster("Public Subnet", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
                alb = ElbApplicationLoadBalancer("ALB")
                nat = NATGateway("NAT")

            with Cluster("Private Subnet", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
                asg = AutoScaling("Auto Scaling")

            with Cluster("Private Subnet                    ", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
                with Cluster("Subnet1", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
                    rds_primary = RDS("DB Primary")
                with Cluster("Subnet2", graph_attr={"fontsize": "18", "fontname": "Arial Bold"}):
                    rds_standby = RDS("DB Standby")

    # Traffic Flow - Top to Bottom
    users >> Edge(color="#1f77b4", fontname="Arial Bold", fontsize="14") >> igw >> Edge(color="#1f77b4", fontname="Arial Bold", fontsize="14") >> alb >> Edge(color="#2ca02c", fontname="Arial Bold", fontsize="14") >> asg >> Edge(color="#d62728", fontname="Arial Bold", fontsize="14") >> rds_primary

    # Database replication
    rds_primary >> Edge(label="Sync", style="dashed", color="#9467bd", fontname="Arial Bold", fontsize="14") >> rds_standby

    # Outbound internet access
    asg >> Edge(color="#ff7f0e", fontname="Arial Bold", fontsize="14") >> nat >> Edge(color="#ff7f0e", fontname="Arial Bold", fontsize="14") >> igw