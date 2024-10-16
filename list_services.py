import os
import sys
import yaml
from typing import List, Dict, Optional


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


def main(main_output: str = "index.yml", secondary_output: str = "README.md") -> None:
    base_dir = "."  # Adjust this if your directory is different
    all_services: List[Dict[str, str]] = []
    processed_paths = set()

    for root, dirs, files in os.walk(base_dir):
        if "docker-compose.yml" in files:
            file_path = os.path.join(root, "docker-compose.yml")
            if file_path not in processed_paths:
                port = extract_first_service_and_port(file_path)
                if port:
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

    # YAML output with a new line after each service block
    output = "---\n" + "\n\n".join(
        f"- name: {service['name']}\n  image: {service['image']}\n  port: {service['port']}\n  path: {service['path']}"
        for service in all_services
    ) + "\n"

    # Write to index.yml (main output)
    with open(main_output, "w") as file:
        file.write(output)

    # Write to README.md (secondary output)
    with open(secondary_output, "w") as file:
        file.write(output)

    print(f"Output written to {main_output} and {secondary_output}")


if __name__ == "__main__":
    main_output_file = sys.argv[1] if len(sys.argv) > 1 else "index.yml"
    secondary_output_file = sys.argv[2] if len(sys.argv) > 2 else "README.md"
    main(main_output=main_output_file, secondary_output=secondary_output_file)

