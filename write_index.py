import os
import yaml
from typing import List, Dict, Optional


# Hardcoded output files
OUTPUT = "index.yml"
README = "README.md"


def extract_first_service_and_port(file_path: str) -> Optional[int]:
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    services = data.get("services", {})
    if services:
        first_service_info = next(iter(services.values()))
        ports = first_service_info.get("ports", [])
        if ports:
            host_port = ports[0].split(":")[0]
            return int(host_port)
    return None


def main() -> None:
    base_dir = "."  # Adjust this if your directory is different
    all_services: List[Dict[str, str]] = []
    processed_paths = set()
    used_ports = set()

    for root, dirs, files in os.walk(base_dir):
        if "docker-compose.yml" in files:
            file_path = os.path.join(root, "docker-compose.yml")
            if file_path not in processed_paths:
                port = extract_first_service_and_port(file_path)
                if port:
                    if port in used_ports:
                        print(f"Warning: Duplicate port {port} found in {file_path}")
                    else:
                        used_ports.add(port)

                    path_parts = root.split(os.sep)
                    image_name = path_parts[-2] if len(path_parts) > 1 else "."
                    container_name = path_parts[-1]
                    relative_path = os.path.relpath(file_path, base_dir)
                    all_services.append({
                        "name": container_name,
                        "image": image_name,
                        "port": str(port),
                        "path": relative_path
                    })
                    processed_paths.add(file_path)

    all_services.sort(key=lambda x: int(x["port"]))

    # YAML output as a list of items with a newline between each item
    output = "\n\n".join(
        yaml.dump([service], default_flow_style=False).strip() for service in all_services
    ) + "\n"

    # Write to index.yml (OUTPUT)
    with open(OUTPUT, "w") as file:
        file.write(output)

    # Write to README.md (README) enclosed in a code block
    with open(README, "w") as file:
        file.write(f"```\n{output}\n```")

    print(f"Output written to {OUTPUT} and {README}")


if __name__ == "__main__":
    main()

