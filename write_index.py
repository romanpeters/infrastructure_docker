import os
import yaml
from typing import List, Dict, Optional

class AnsibleDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(AnsibleDumper, self).increase_indent(flow, False)

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
                    # Change relative_path to only include directory structure
                    relative_path = os.path.relpath(root, base_dir)  # Get only the directory part
                    all_services.append({
                        "name": container_name,
                        "image": image_name,
                        "port": str(port),
                        "path": relative_path  # Use the modified relative_path
                    })
                    processed_paths.add(file_path)

    all_services.sort(key=lambda x: int(x["port"]))

    # Prepare YAML output with starting line
    yaml_output = {"infrastructure_docker": all_services}

    # Use AnsibleDumper for proper formatting
    formatted_output = yaml.dump(
        yaml_output,
        Dumper=AnsibleDumper,
        default_flow_style=False,
        sort_keys=False
    )

    # Write to index.yml (OUTPUT)
    with open(OUTPUT, "w") as file:
        file.write(formatted_output.strip() + "\n")  # Ensure no extra newline at end

    # Write to README.md (README) enclosed in a code block
    with open(README, "w") as file:
        file.write(f"```\n{formatted_output.strip()}\n```\n")  # Ensure no extra newline at end

    print(f"Output written to {OUTPUT} and {README}")

if __name__ == "__main__":
    main()

