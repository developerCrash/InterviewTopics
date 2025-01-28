import re

def parse_ospf_neighbors(output):
    """
    Parses OSPF neighbors from router output.

    :param output: str, router command output (e.g., `show ip ospf neighbor`)
    :return: list of dictionaries, each containing neighbor details
    """
    # Regular expression to capture OSPF neighbor details
    neighbor_pattern = re.compile(
        r"^(\S+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)$"
    )

    neighbors = []
    lines = output.splitlines()

    for line in lines:
        match = neighbor_pattern.match(line)
        if match:
            neighbors.append({
                "Neighbor ID": match.group(1),
                "Priority": int(match.group(2)),
                "State": match.group(3),
                "Dead Time": match.group(4),
                "Address": match.group(5)
            })

    return neighbors

# Example usage
if __name__ == "__main__":
    ospf_output = """
    Neighbor ID     Pri   State           Dead Time   Address         Interface
    10.1.1.1          1   FULL/DR         00:00:32    192.168.1.1     GigabitEthernet0/0
    10.2.2.2          1   FULL/BDR        00:00:31    192.168.1.2     GigabitEthernet0/1
    10.3.3.3          1   2WAY/DROTHER    00:00:30    192.168.1.3     GigabitEthernet0/2
    """

    parsed_neighbors = parse_ospf_neighbors(ospf_output)

    for neighbor in parsed_neighbors:
        print(neighbor)
